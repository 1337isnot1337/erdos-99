#!/usr/bin/env python3
"""Exact wall and three-guard regressions in Q(sqrt(3)).

The universal local exclusion uses the report's Taylor argument.
Samples certify no arbitrary capacity upper bound or global optimizer.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json


@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(value):
        return value if isinstance(value,Q) else Q(F(value))

    def __add__(self,other):
        other = Q.of(other)
        return Q(self.a+other.a,self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a,-self.b)

    def __sub__(self,other):
        return self+-Q.of(other)

    def __rsub__(self,other):
        return Q.of(other)+-self

    def __mul__(self,other):
        other = Q.of(other)
        return Q(self.a*other.a+3*self.b*other.b,
                 self.a*other.b+self.b*other.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a>0)-(self.a<0)
        if not self.a:
            return (self.b>0)-(self.b<0)
        if (self.a>0) == (self.b>0):
            return 1 if self.a>0 else -1
        difference = self.a*self.a-3*self.b*self.b
        assert difference
        return ((self.a>0)-(self.a<0))*(1 if difference>0 else -1)


def add(p,q):
    return p[0]+q[0],p[1]+q[1]


def sub(p,q):
    return p[0]-q[0],p[1]-q[1]


def scale(p,a):
    return p[0]*a,p[1]*a


def mul(p,q):
    return p[0]*q[0]-p[1]*q[1],p[0]*q[1]+p[1]*q[0]


def power(r,n):
    if n<0:
        r,n=(r[0],-r[1]),-n
    result = F(1),F(0)
    while n:
        if n%2:
            result=mul(result,r)
        r,n=mul(r,r),n//2
    return result


def norm(p):
    return p[0]*p[0]+p[1]*p[1]


def distance(p,q):
    return norm(sub(p,q))


def cross(p,q):
    return p[0]*q[1]-p[1]*q[0]


def case(m):
    t=F(1,10**8*m**4)
    rotation=((1-t*t)/(1+t*t),2*t/(1+t*t))
    a=Q(F(0),F(1,2))
    bases=[(Q(F(-1,2)),a),(Q(-1),Q()),(Q(F(-1,2)),-a),
           (Q(F(1,2)),-a),(Q(1),Q()),(Q(F(1,2)),a)]
    offsets=[power(rotation,2*j-m+1) for j in range(m)]
    length=sum(r[0] for r in offsets)
    assert sum(r[1] for r in offsets)==0 and 0<length<m
    corner=(Q(length),Q())
    edges=[mul(r,w) for w in bases for r in offsets]
    wall=[corner]
    for e in edges[:-1]:
        wall.append(add(wall[-1],e))
    assert add(wall[-1],edges[-1])==corner
    assert wall[1]==add(corner,mul(power(rotation,-(m-1)),bases[0]))
    assert wall[-1]==sub(corner,mul(power(rotation,m-1),bases[-1]))
    contacts={tuple(sorted((i,(i+1)%(6*m)))) for i in range(6*m)}
    wall_pair_checks=0
    for i,j in combinations(range(6*m),2):
        d=distance(wall[i],wall[j])
        assert d==Q(1) if (i,j) in contacts else (d-1).sign()>0
        wall_pair_checks+=1
    convexity_checks=0
    for i,e in enumerate(edges):
        assert norm(e)==Q(1)
        for j,p in enumerate(wall):
            if j not in (i,(i+1)%(6*m)):
                assert cross(e,sub(p,wall[i])).sign()>0
                convexity_checks+=1
    counts={'corner':0,'predecessor':0,'successor':0}
    proposals=0
    for numerator in range(-20,21):
        kappa=F(numerator,10)
        phi_t=kappa*t
        phi=((1-phi_t*phi_t)/(1+phi_t*phi_t),
             2*phi_t/(1+phi_t*phi_t))
        for lam in (0,1,10):
            ell=1+lam*t*t
            p=mul(phi,(Q(ell*(m-1)),Q()))
            failures=[name for name,q in [('corner',wall[0]),
                                          ('predecessor',wall[-1]),
                                          ('successor',wall[1])]
                      if (distance(p,q)-1).sign()<0]
            assert failures,(m,kappa,lam)
            for name in failures:
                counts[name]+=1
            proposals+=1
    return {'M':m,'wall_vertices':6*m,'wall_pair_checks':wall_pair_checks,
            'convexity_checks':convexity_checks,'homothety_proposals':proposals,
            'failed_guard_counts':counts,
            'old_wall_scope':'feasible triangle-free; no canonical rank or optimality'}


def affine_trace_identities():
    a=Q(F(0),F(1,2))
    directions=[(Q(1),Q()),(Q(F(1,2)),a),(Q(F(-1,2)),a)]
    xx=sum(r[0]*r[0] for r in directions)
    xy=sum(r[0]*r[1] for r in directions)
    yy=sum(r[1]*r[1] for r in directions)
    assert xx==yy==Q(F(3,2)) and xy==Q()
    determinant=Q(F(0),F(3,4))
    assert determinant.sign()>0
    # Three quadratic evaluation rows determine a symmetric 2x2 form.
    rows=[(r[0]*r[0],2*r[0]*r[1],r[1]*r[1]) for r in directions]
    det=(rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])
         -rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])
         +rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]))
    assert det==determinant
    for m in range(3,101):
        c=F(m*(m*m-1),6)
        assert F(m+1,3)>1
        assert m*(m-1)-2*c == -F(m*(m-1)*(m-2),3)<0
        assert 6*m*(m-1)-12*c == -2*m*(m-1)*(m-2)<0
    return {'quadratic_form_evaluation_rank':3,
            'direction_outer_product_sum':'(3/2) I',
            'negative_coefficient_cases':98}


def main():
    cases=[case(m) for m in (3,4,6,8)]
    print(json.dumps({'classification':'restricted packet corner regressions',
                      'cases':cases,
                      'wall_pair_checks':sum(c['wall_pair_checks'] for c in cases),
                      'homothety_proposals':sum(c['homothety_proposals'] for c in cases),
                      'affine_trace_identities':affine_trace_identities(),
                      'not_proved':['arbitrary packet capacity upper bound',
                                    'global optimality','remote affine motion exclusion',
                                    'nonaffine packet exclusion','C-II or Level I']},sort_keys=True))


if __name__=='__main__':
    main()
