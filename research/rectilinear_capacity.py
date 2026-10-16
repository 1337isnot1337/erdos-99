"""Exact finite capacity for rectilinear strained triangular patches.

The points in this module have the form

    x_i * e1 + y_j * e2,

where ``e1`` and ``e2`` are unit vectors making a 60 degree angle and the
coordinate chains have consecutive gaps at least one.  The source need not be
homothetically strained or equally spaced.  Its convex hull is a parallelogram,
and an integer triangular-lattice patch can be placed in that hull using only the
two total coordinate spans.

This is a finite capacity instrument.  It does not assert that an exterior point
set remains separated from the replacement lattice patch; that is the protected
replacement hypothesis recorded in the canonical theorem state.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import floor
from typing import Iterable


Scalar = int | Fraction


def _clamp(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    return min(max(value, lower), upper)


def _as_fraction_chain(values: Iterable[Scalar]) -> tuple[Fraction, ...]:
    chain = tuple(Fraction(value) for value in values)
    if len(chain) < 2:
        raise ValueError("each coordinate chain must contain at least two values")
    if any(next_value <= value for value, next_value in zip(chain, chain[1:])):
        raise ValueError("coordinate chains must be strictly increasing")
    if any(next_value - value < 1 for value, next_value in zip(chain, chain[1:])):
        raise ValueError("consecutive coordinate gaps must be at least one")
    return chain


def triangular_norm_squared(first: Fraction, second: Fraction) -> Fraction:
    """Return ``|first*e1 + second*e2|^2`` for a 60 degree basis."""

    return first * first + first * second + second * second


def short_diagonal_squared(first_gap: Fraction, second_gap: Fraction) -> Fraction:
    """Return the squared short diagonal of a coordinate cell.

    A cell with side gaps ``a`` and ``b`` has the diagonal ``a*e1-b*e2``;
    its squared length is ``a**2-a*b+b**2``.
    """

    if first_gap <= 0 or second_gap <= 0:
        raise ValueError("cell gaps must be positive")
    return (
        first_gap * first_gap
        - first_gap * second_gap
        + second_gap * second_gap
    )


def point_to_cell_distance_squared(
    first: Fraction,
    second: Fraction,
    first_lower: Fraction,
    first_upper: Fraction,
    second_lower: Fraction,
    second_upper: Fraction,
) -> Fraction:
    """Return the exact squared distance to an oblique coordinate cell.

    The cell is [first_lower, first_upper] * e1 + [second_lower, second_upper] * e2.
    The Euclidean metric in these coordinates is u**2 + u*v + v**2.  The closest
    point is either the query point itself or lies on one of the four cell edges;
    each edge projection is rational.
    """

    if first_lower > first_upper or second_lower > second_upper:
        raise ValueError("cell bounds must be ordered")
    if (
        first_lower <= first <= first_upper
        and second_lower <= second <= second_upper
    ):
        return Fraction(0)

    candidates: list[Fraction] = []
    for fixed_first in (first_lower, first_upper):
        first_difference = first - fixed_first
        projected_second = _clamp(
            second + first_difference / 2,
            second_lower,
            second_upper,
        )
        candidates.append(
            triangular_norm_squared(
                first_difference,
                second - projected_second,
            )
        )

    for fixed_second in (second_lower, second_upper):
        second_difference = second - fixed_second
        projected_first = _clamp(
            first + second_difference / 2,
            first_lower,
            first_upper,
        )
        candidates.append(
            triangular_norm_squared(
                first - projected_first,
                second_difference,
            )
        )

    return min(candidates)


def point_to_cell_boundary_distance_squared(
    first: Fraction,
    second: Fraction,
    first_lower: Fraction,
    first_upper: Fraction,
    second_lower: Fraction,
    second_upper: Fraction,
) -> Fraction:
    """Return the exact squared distance to the boundary of a coordinate cell."""

    if first_lower > first_upper or second_lower > second_upper:
        raise ValueError("cell bounds must be ordered")
    distances: list[Fraction] = []
    for fixed_first in (first_lower, first_upper):
        first_difference = first - fixed_first
        projected_second = _clamp(
            second + first_difference / 2,
            second_lower,
            second_upper,
        )
        distances.append(
            triangular_norm_squared(
                first_difference,
                second - projected_second,
            )
        )
    for fixed_second in (second_lower, second_upper):
        second_difference = second - fixed_second
        projected_first = _clamp(
            first + second_difference / 2,
            first_lower,
            first_upper,
        )
        distances.append(
            triangular_norm_squared(
                first - projected_first,
                second_difference,
            )
        )
    return min(distances)


@dataclass(frozen=True)
class RectilinearPatch:
    """A finite product patch in two 60 degree coordinate directions.

    ``x`` and ``y`` are exact coordinate chains.  The source has
    ``len(x) * len(y)`` points.  The candidate lattice patch is based at the
    lower-left source corner and uses every integer coordinate up to the floor
    of each total span.
    """

    x: tuple[Fraction, ...]
    y: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        normalized_x = _as_fraction_chain(self.x)
        normalized_y = _as_fraction_chain(self.y)
        object.__setattr__(self, "x", normalized_x)
        object.__setattr__(self, "y", normalized_y)

    @classmethod
    def from_values(
        cls, x: Iterable[Scalar], y: Iterable[Scalar]
    ) -> "RectilinearPatch":
        """Construct a patch while normalizing all coordinates to Fractions."""

        return cls(_as_fraction_chain(x), _as_fraction_chain(y))

    @property
    def rows(self) -> int:
        return len(self.x)

    @property
    def columns(self) -> int:
        return len(self.y)

    @property
    def span_x(self) -> Fraction:
        return self.x[-1] - self.x[0]

    @property
    def span_y(self) -> Fraction:
        return self.y[-1] - self.y[0]

    @property
    def extra_layers_x(self) -> int:
        """Number of complete integer layers exposed in the first direction."""

        return floor(self.span_x) - (self.rows - 1)

    @property
    def extra_layers_y(self) -> int:
        """Number of complete integer layers exposed in the second direction."""

        return floor(self.span_y) - (self.columns - 1)

    @property
    def source_size(self) -> int:
        return self.rows * self.columns

    @property
    def candidate_shape(self) -> tuple[int, int]:
        """Return the candidate's numbers of integer coordinates in each direction."""

        return (floor(self.span_x) + 1, floor(self.span_y) + 1)

    @property
    def candidate_size(self) -> int:
        width, height = self.candidate_shape
        return width * height

    @property
    def gain(self) -> int:
        """Return candidate size minus source size."""

        return self.candidate_size - self.source_size

    @property
    def source_diameter_squared(self) -> Fraction:
        """Return the exact source diameter squared."""

        return triangular_norm_squared(self.span_x, self.span_y)

    @property
    def candidate_diameter_squared(self) -> Fraction:
        """Return the exact diameter squared of the candidate lattice patch."""

        width, height = self.candidate_shape
        return triangular_norm_squared(Fraction(width - 1), Fraction(height - 1))

    @property
    def candidate_fits(self) -> bool:
        """Whether the candidate's diameter does not exceed the source's."""

        return self.candidate_diameter_squared <= self.source_diameter_squared

    @property
    def boundary_safe_shape(self) -> tuple[int, int]:
        """Return a lattice core more than one unit from every hull side.

        A lattice point with at least two integer coordinate steps from each
        side of the coordinate parallelogram is at perpendicular distance at
        least ``sqrt(3)`` from every side.  The returned shape is therefore
        automatically separated from any point outside the open hull.
        """

        width, height = self.candidate_shape
        return (max(width - 4, 0), max(height - 4, 0))

    @property
    def boundary_safe_candidate_size(self) -> int:
        """Return the number of automatically exterior-protected sites."""

        width, height = self.boundary_safe_shape
        return width * height

    @property
    def boundary_safe_capacity(self) -> bool:
        """Whether the protected core has enough sites by cardinality.

        The word ``safe`` refers only to separation from points outside the
        open coordinate hull.  This boolean does *not* certify separation from
        arbitrary points of an ambient source that remain inside the hull; that
        is the unresolved exterior-protection step in Target A.
        """

        return self.boundary_safe_candidate_size >= self.source_size

    @property
    def candidate_is_unit_separated(self) -> bool:
        """The integer triangular-lattice candidate is always unit-separated."""

        return True

    @property
    def cell_short_diagonal_squared(self) -> tuple[tuple[Fraction, ...], ...]:
        """Return the short-diagonal square for every coordinate cell."""

        x_gaps = tuple(
            self.x[i + 1] - self.x[i] for i in range(self.rows - 1)
        )
        y_gaps = tuple(
            self.y[j + 1] - self.y[j] for j in range(self.columns - 1)
        )
        return tuple(
            tuple(
                short_diagonal_squared(first_gap, second_gap)
                for second_gap in y_gaps
            )
            for first_gap in x_gaps
        )

    @property
    def bad_cell_indices(self) -> tuple[tuple[int, int], ...]:
        """Return cells not certified by strict open unit coverage.

        A bad cell is one with short-diagonal square at least three.  By the
        cellwise coverage theorem, every possible additional source point in
        the open product hull must lie in the union of these closed cells.
        """

        return tuple(
            (first_index, second_index)
            for first_index, row in enumerate(self.cell_short_diagonal_squared)
            for second_index, value in enumerate(row)
            if value >= 3
        )

    @property
    def cellwise_protected_candidate_indices(self) -> tuple[tuple[int, int], ...]:
        """Return lattice indices protected from bad cells and the hull boundary.

        The returned candidate site (a, b) denotes
        (x[0] + a) * e1 + (y[0] + b) * e2.  It is retained only when its
        exact distance to the product-hull boundary and to every closed bad cell
        is at least one.  Consequently it is separated from any exterior source
        point: good-cell interiors are excluded by strict unit coverage, while
        all remaining source points lie in a bad cell or outside the open hull.
        """

        width, height = self.candidate_shape
        bad_cells = self.bad_cell_indices
        protected: list[tuple[int, int]] = []
        for first_index in range(width):
            first = self.x[0] + first_index
            for second_index in range(height):
                second = self.y[0] + second_index
                if (
                    point_to_cell_boundary_distance_squared(
                        first,
                        second,
                        self.x[0],
                        self.x[-1],
                        self.y[0],
                        self.y[-1],
                    )
                    < 1
                ):
                    continue
                if any(
                    point_to_cell_distance_squared(
                        first,
                        second,
                        self.x[first_cell],
                        self.x[first_cell + 1],
                        self.y[second_cell],
                        self.y[second_cell + 1],
                    )
                    < 1
                    for first_cell, second_cell in bad_cells
                ):
                    continue
                protected.append((first_index, second_index))
        return tuple(protected)

    @property
    def cellwise_protected_candidate_size(self) -> int:
        """Return the exact count of protected candidate sites."""

        return len(self.cellwise_protected_candidate_indices)

    @property
    def cellwise_protected_capacity(self) -> bool:
        """Whether the bad-cell-safe candidate can replace the source patch."""

        return self.cellwise_protected_candidate_size >= self.source_size

    @property
    def interior_unit_covering(self) -> bool:
        """Whether every interior hull point is strictly within one unit.

        The cells are rhombi with side gaps from the two coordinate chains.  If
        every short diagonal has squared length strictly below three, each cell
        is covered strictly by the open unit disks around its four corners.
        Thus this property excludes an additional unit-separated point from the
        interior of the product hull.  It says nothing about points on the hull
        boundary or about an ambient source point elsewhere inside a larger hull.
        """

        x_gaps = (self.x[i + 1] - self.x[i] for i in range(self.rows - 1))
        y_gaps = (self.y[j + 1] - self.y[j] for j in range(self.columns - 1))
        return all(
            short_diagonal_squared(first_gap, second_gap) < 3
            for first_gap in x_gaps
            for second_gap in y_gaps
        )

    @property
    def closed_unit_covering(self) -> bool:
        """Whether the closed unit disks cover the complete coordinate hull."""

        return all(
            short_diagonal_squared(first_gap, second_gap) <= 3
            for first_gap in (self.x[i + 1] - self.x[i] for i in range(self.rows - 1))
            for second_gap in (
                self.y[j + 1] - self.y[j] for j in range(self.columns - 1)
            )
        )


def homothetic_patch(
    side: int, x_scale: Fraction, y_scale: Fraction
) -> RectilinearPatch:
    """Return an exact equally spaced patch with possibly different scales."""

    if side < 2:
        raise ValueError("side must be at least 2")
    if x_scale < 1 or y_scale < 1:
        raise ValueError("coordinate scales must be at least one")
    return RectilinearPatch.from_values(
        (x_scale * i for i in range(side)),
        (y_scale * j for j in range(side)),
    )


if __name__ == "__main__":
    patch = homothetic_patch(10, Fraction(1), Fraction(4, 3))
    print(
        {
            "source_size": patch.source_size,
            "candidate_size": patch.candidate_size,
            "gain": patch.gain,
            "extra_layers": (patch.extra_layers_x, patch.extra_layers_y),
            "candidate_fits": patch.candidate_fits,
        }
    )
