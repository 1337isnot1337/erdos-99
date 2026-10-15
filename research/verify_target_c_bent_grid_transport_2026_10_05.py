#!/usr/bin/env python3
"""Exact Q(sqrt(3)) checks of the bent-grid transport regression.
No diameter loading or global optimality is certified.
"""
from fractions import Fraction as F


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def scale(x, t):
    return (x[0]*t, x[1]*t)


def sign(x):
    a,b=x
    if not b:
        return (a>0)-(a<0)
    if not a or (a>0)==(b>0):
        return (b>0)-(b<0)
    d=a*a-3*b*b
    s=(d>0)-(d<0)
    return s if a>0 else -s


def squared_distance(p,q):
    x=add(p[0],neg(q[0]));y=add(p[1],neg(q[1]))
    return add(mul(x,x),mul(y,y))


def run(m):
    assert m>=8 and m%2==0
    z=(F(0),F(0));one=(F(1),F(0))
    t=F(1,m);c=(1-t*t)/(1+t*t);s=2*t/(1+t*t)
    v=((c/2,-s/2),(s/2,c/2))
    assert add(mul(v[0],v[0]),mul(v[1],v[1]))==one
    u=[];prefix=[(F(0),F(0))]
    for i in range(m):
        t=F(i,2*m*m)
        a=(1-t*t)/(1+t*t);b=2*t/(1+t*t)
        assert a*a+b*b==1
        u.append((a,b));prefix.append((prefix[-1][0]+a,prefix[-1][1]+b))
    points=[(((prefix[i][0],F(0)),(prefix[i][1],F(0))),i,j)
            for i in range(m+1) for j in range(m+1)]
    points=[((add(p[0],scale(v[0],F(j))),add(p[1],scale(v[1],F(j)))),i,j)
            for p,i,j in points]
    contacts=0;pairs=0
    for a,(p,i,j) in enumerate(points):
        for q,k,l in points[a+1:]:
            d=squared_distance(p,q);expected=abs(i-k)+abs(j-l)==1
            if expected:
                assert d==one,(m,i,j,k,l,d)
                contacts+=1
            else:
                assert sign(add(d,neg(one)))>0,(m,i,j,k,l,d)
            pairs+=1
    assert contacts==2*m*(m+1)
    bow=prefix[m][1]/2-prefix[m//2][1]
    assert bow>=F(1,8)-F(1,4*m*m)>F(1,10)
    excess=z
    for a,b in u:
        determinant=add(scale(v[1],a),neg(scale(v[0],b)))
        e=add(determinant,(F(0),F(-1,2)))
        assert sign(e)>0
        excess=add(excess,scale(e,F(m)))
    assert sign(excess)>0 and sign(add((F(2*m),F(0)),neg(excess)))>0
    print(f'M={m}: points={len(points)}, pairs={pairs}, contacts={contacts}, '
          f'rhombi={m*m}; exact bow > 1/10 and 0<E4<2M',flush=True)
    return pairs


if __name__=='__main__':
    total=sum(run(m) for m in (8,12,16))
    print(f'PASS: {total} pair checks over Q(sqrt(3)). '
          'No actual diameter loads or global minimum is asserted.')
