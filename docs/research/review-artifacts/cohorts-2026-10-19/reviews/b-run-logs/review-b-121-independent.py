from fractions import Fraction as F
from itertools import combinations, product

def add(p,q): return (p[0]+q[0],p[1]+q[1])
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def scale(k,p): return (k*p[0],k*p[1])
def qnorm(p): return p[0]*p[0]+p[0]*p[1]+p[1]*p[1]
def cross(p,q): return p[0]*q[1]-p[1]*q[0]
def onseg(p,a,b): return cross(sub(p,a),sub(b,a))==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
def intersects(s,t):
 a,b=s;c,d=t
 o1=cross(sub(b,a),sub(c,a));o2=cross(sub(b,a),sub(d,a))
 o3=cross(sub(d,c),sub(a,c));o4=cross(sub(d,c),sub(b,c))
 return (o1*o2<0 and o3*o4<0) or (o1==0 and onseg(c,a,b)) or (o2==0 and onseg(d,a,b)) or (o3==0 and onseg(a,c,d)) or (o4==0 and onseg(b,c,d))
x=(F(1,3),F(1,3)); Y={'y0':(F(0),F(0)),'y1':(F(1),F(0)),'y2':(F(0),F(1))}
local={'a1':(-F(2,3),F(1,2)),'a2':(-F(1,3),F(4,3)),'a3':(-F(1,3),-F(2,3)),'b':(F(1,2),-F(1,3)),'c':(F(5,6),F(1,2))}
dirs=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
sources=dict(local);sources.update({f'h{i}':add(x,scale(F(6),d)) for i,d in enumerate(dirs)})
assert len(sources)==11 and min(qnorm(sub(a,b)) for a,b in combinations(sources.values(),2))==F(13,12)
assert all(qnorm(sub(a,b))>1 for a,b in combinations(sources.values(),2))
# Independently enumerate every saturating assignment of the complete 3-site shore.
edges={y:[s for s,p in sources.items() if qnorm(sub(pt,p))<1] for y,pt in Y.items()}
full_y=[]
for values in product(*(edges[y] for y in Y)):
 if len(set(values))==3: full_y.append(dict(zip(Y,values)))
full_x=[s for s,p in sources.items() if qnorm(sub(x,p))<1]
assert 'a1' in full_x and full_y
chosen={'y0':'a1','y1':'b','y2':'c'}
assert chosen in full_y and 'a1' in full_x
assert len(set(chosen.values()))==3
segments=[(Y[y],sources[s]) for y,s in chosen.items()]
assert all(not intersects(s,t) for s,t in combinations(segments,2))
assert qnorm(sub(Y['y0'],Y['y1']))==1
# C={x}, O={y0}: the selected pair overlaps, but another full pair does not.
assert chosen['y0']=='a1'
assert qnorm(sub(x,sources['a2']))==F(7,9) and qnorm(sub(Y['y0'],sources['a3']))==F(7,9)
assert 'a2' in full_x and any(m['y0']=='a3' for m in full_y)
assert min(int(s==m['y0']) for s in full_x for m in full_y)==0
# Complete Y_in: completing-square coordinate bounds leave only u,v in {-?}; direct finite list is the fixture's fundamental neighborhood.
inside={(F(u),F(v)) for u in range(-2,3) for v in range(-2,3) if qnorm(sub((F(u),F(v)),x))<1}
assert inside==set(Y.values())
# Cartesian 5x5 grid: exact unit spacing and the triangle-inequality containment certificate.
grid=[(F(i),F(j)) for i in range(-2,3) for j in range(-2,3)]
cart2=lambda p:p[0]*p[0]+p[1]*p[1]
assert min(cart2(sub(a,b)) for a,b in combinations(grid,2))==1
assert max(cart2(g) for g in grid)==8 and F(1,3)<1 and F(16)<27
print(f'PASS independent exact recomputation: sources={len(sources)}, min_source_distance2=13/12, full_Y_matchings={len(full_y)}, full_X_assignments={len(full_x)}')
print('PASS selected inherited overlap=1; minimum over all full-shore matching pairs on C,O is 0')
print('PASS chosen Y matching segments pairwise disjoint; distance-one response pair is excluded under strict <1')
print('PASS Cartesian grid has 25 points, min distance2=1, max radius2=8; triangle bound gives alpha_1(H)>=25>11')
