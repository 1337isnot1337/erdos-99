#!/usr/bin/env python3
"""Exact finite pair ledgers for the diffuse one-deficit nonglobal family."""
from fractions import Fraction as F
from itertools import combinations
import json


def sign(a,b,d):
    if not b:
        return (a>0)-(a<0)
    if not a:
        return (b>0)-(b<0)
    if (a>0)==(b>0):
        return 1 if a>0 else -1
    gap=a*a-d*b*b
    if not gap:
        return 0
    return ((a>0)-(a<0))*(1 if gap>0 else -1)


def case(m):
    d=m**4-6*m*m-3
    assert d>0 and d<m**4
    points=[(i,j) for i in range(m+1) for j in range(m+1)]
    old_contacts=new_contacts=checks=0
    for p,q in combinations(points,2):
        i,j=p[0]-q[0],p[1]-q[1]
        a,b=F(i*i+j*j),F(i*j,m*m)
        lower=sign(a-1,b,d)
        assert lower>=0
        assert sign(2*m*m-a,1-b,d)>=0
        new=i*i+j*j
        assert new>=1 and sign(2*m*m-new,1,d)>0
        old_contacts+=lower==0
        new_contacts+=new==1
        assert (lower==0)==(abs(i)+abs(j)==1)
        checks+=1
    assert old_contacts==new_contacts==2*m*(m+1)
    # Algebraic normalization and exact area-form deficit coefficient.
    assert d+3*(m*m+1)**2==4*m**4
    assert 2*(m-1)**2+4*m-2==2*m*m
    return {'M':m,'cardinality':len(points),'old_and_new_pair_checks':checks,
            'contacts_each':old_contacts,'triangles_each':0,
            'old_D_squared':[str(2*m*m),'1',d],
            'new_D_squared':2*m*m,'area_deficit':'sqrt(3)/2',
            'classification':'strict sub-diameter competitor; old family nonglobal'}


def main():
    print(json.dumps({'classification':'exact diffuse-strain regression ledgers',
                      'cases':[case(m) for m in (3,4,7,10)],
                      'not_proved':['canonical optimality','vacancy classification',
                                    'C-II or Level I disproof']},sort_keys=True))


if __name__=='__main__':
    main()
