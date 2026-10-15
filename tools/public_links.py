REFERENCE = __import__("re").compile(r"(?m)^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)")
"""Local navigation parser, adapted from the source release tooling."""
import html,posixpath,re
from html.parser import HTMLParser
from pathlib import PurePosixPath
from urllib.parse import unquote,urlsplit
def safe_path(path: str) -> str:
    """Require a portable, normalized path before joining it to any root."""
    if (not isinstance(path, str) or not path or "\\" in path or ":" in path
            or any(ord(c) < 32 or ord(c) == 127 for c in path)
            or PurePosixPath(path).is_absolute()
            or any(p in {"", ".", ".."} or p.lower() == ".git" for p in path.split("/"))):
        raise ValueError(f"unsafe release path: {path!r}")
    return path

def local_target(source: str, target: str, *, markdown_escaped: bool = True) -> str | None:
    # CommonMark destinations may contain entity references and escaped ASCII
    # punctuation, including parentheses in otherwise ordinary filenames.
    if markdown_escaped:
        target = re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", html.unescape(target.strip("<>")))
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path)
    result = posixpath.normpath(path.lstrip("/") if path.startswith("/") else
                               posixpath.join(posixpath.dirname(source), path))
    if result == ".." or result.startswith("../"):
        raise ValueError(f"link escapes release tree in {source}")
    return result

def strip_fenced_code(text: str) -> str:
    """Mask fences while retaining offsets for exact destination-only rewrites."""
    visible = []
    fence_char = None
    fence_length = 0
    opening = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*?)(?:\r?\n)?$")
    for line in text.splitlines(keepends=True):
        if fence_char is None:
            match = opening.match(line)
            if not match:
                visible.append(line)
                continue
            fence = match.group(1)
            info = match.group(2)
            # CommonMark forbids backticks in a backtick-fence info string.
            if fence[0] == "`" and "`" in info:
                visible.append(line)
                continue
            fence_char, fence_length = fence[0], len(fence)
            visible.append(mask(line))
            continue

        close = re.fullmatch(
            rf" {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*(?:\r?\n)?",
            line,
        )
        if close:
            fence_char, fence_length = None, 0
        visible.append(mask(line))
        # All content through the matching close is example text, not navigation.
    return "".join(visible)

def navigation_text(text: str) -> str:
    """Mask examples and mathematics while preserving source offsets."""
    text = strip_fenced_code(text)
    runs = list(re.finditer(r"`+", text))
    next_equal, last = {}, {}
    for i in range(len(runs)-1, -1, -1):
        length = len(runs[i][0])
        if length in last:
            next_equal[i] = last[length]
        last[length] = i
    i = 0
    while i < len(runs):
        opening = runs[i]
        escaped = len(text[:opening.start()]) - len(text[:opening.start()].rstrip("\\"))
        if i not in next_equal or escaped % 2:
            i += 1
            continue
        close = next_equal[i]
        a, b = opening.start(), runs[close].end()
        # Inline parsing ends at a paragraph/block boundary. An unmatched
        # historical backtick must not swallow dependencies in later prose.
        if re.search(r"\r?\n[ \t]*\r?\n|(?m:^ {0,3}#{1,6}[ \t])", text[a:b]):
            i += 1
            continue
        text = text[:a] + mask(text[a:b]) + text[b:]
        i = close + 1
    text = re.sub(r"(?s)(?<![\w\\])\\\[.*?\\\]|\$\$.*?\$\$|(?<![\w\\])\\\(.*?\\\)|<!--.*?-->",
                  lambda m: mask(m[0]), text)
    return text

def markdown_destinations(text: str):
    """Yield source spans for inline links and conservative reference definitions."""
    text = navigation_text(text)
    stack, spans = [], []
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if char == "[":
            stack.append(i)
        elif char == "]" and stack:
            stack.pop()
            if text[i+1:i+2] == "(":
                start = i + 2
                while start < len(text) and text[start].isspace():
                    start += 1
                end, depth = start, 0
                angle = text[start:start+1] == "<"
                if angle:
                    end = text.find(">", start+1)
                    if end < 0 or "\n" in text[start:end]:
                        i += 1
                        continue
                    end += 1
                else:
                    while end < len(text):
                        c = text[end]
                        if c == "\\":
                            end += 2
                            continue
                        if c == "(":
                            depth += 1
                        elif c == ")":
                            if depth == 0:
                                break
                            depth -= 1
                        elif c.isspace():
                            break
                        end += 1
                tail = re.match(r'''(?:\s+(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\([^()]*\)))?\s*\)''', text[end:])
                if not depth and tail:
                    spans.append((start, end, text[start:end]))
                    i = end + tail.end()
                    continue
        i += 1
    for match in REFERENCE.finditer(text):
        spans.append((*match.span(1), match[1]))
    yield from sorted(spans)

def html_destinations(text: str) -> list[str]:
    class Navigation(HTMLParser):
        def handle_starttag(self, tag, attrs):
            self.destinations.extend(value for key, value in attrs
                                     if key in {"href", "src"} and value)
        handle_startendtag = handle_starttag
    parser = Navigation(convert_charrefs=True)
    parser.destinations = []
    parser.feed(navigation_text(text))
    parser.close()
    return parser.destinations

def markdown_targets(source: str, text: str) -> list[str]:
    raw_targets = [raw for _, _, raw in markdown_destinations(text)]
    targets = [p for raw in raw_targets if (p := local_target(source, raw)) is not None]
    targets.extend(p for raw in html_destinations(text)
                   if (p := local_target(source, raw, markdown_escaped=False)) is not None)
    return targets

def mask(text: str) -> str:
    return re.sub(r"[^\r\n]", " ", text)
