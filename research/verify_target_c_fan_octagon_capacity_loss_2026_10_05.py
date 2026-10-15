"""Exact finite octagon capacity-loss certificates; no global optimality.
Squared distances lie in Q(sqrt((1-epsilon^2)(1-a^2))).
The general wall covering argument is analytic in the companion report.
"""
from fractions import Fraction as F
from itertools import combinations

def check(D):
 e=F(1,2*D); d=e/2; a=1-e/2; t2=1-e*e; h2=1-a*a; rad=t2*h2
 def sign(r,c):
  if not c:return (r>0)-(r<0)
  if not r:return (c>0)-(c<0)
  if (r>0)==(c>0):return (r>0)-(r<0)
  z=r*r-c*c*rad
  return ((r>0)-(r<0))*((z>0)-(z<0))
 def sq(p,q):
  x=p[0]-q[0]; t=p[1]-q[1]; h=p[2]-q[2]
  return x*x+t*t*t2+h*h*h2,2*t*h
 P=[(F(0),0,0),(-e,1,0),(-1-d,1,1),(-2-2*d+e,1,0),(-2-2*d,0,0),(-2-2*d+e,-1,0),(-1-d,-1,-1),(-e,-1,0)]
 old=P+[(-1-d,0,0),(-F(D),0,0)]
 contacts=set(); H=set()
 for i,j in combinations(range(10),2):
  r,c=sq(old[i],old[j]); assert sign(r-1,c)>=0,(D,i,j,r,c)
  assert sign(r-D*D,c)<=0
  if sign(r-1,c)==0:contacts.add((i,j))
  if sign(r-D*D,c)==0:H.add((i,j))
 assert contacts=={tuple(sorted((i,(i+1)%8))) for i in range(8)}
 assert H=={(0,9),(1,9),(7,9)}
 new=P.copy();new[0]=(-2*e,0,0)
 endpoint=new+old[8:]
 failures=set()
 for i,j in combinations(range(10),2):
  r,c=sq(endpoint[i],endpoint[j])
  assert sign(r-D*D,c)<=0
  if sign(r-1,c)<0:failures.add((i,j))
 assert failures=={(0,8)}
 center=(-1-d-e,0,1)
 for v in (new[0],new[4],new[2]):assert sq(center,v)==(1,0)
 for r,c in ((e*a,-1),(-e*a,-1)):
  assert sign(r+F(1,2),c)>0
 assert sq(new[0],old[8])[0]<1
 return 45
if __name__ == "__main__":
 count=sum(check(D) for D in (10,20,100,1000,10000))
 print(f"PASS: {count} old and {count} reflected source-pair certificates; exact contacts, diameters, sole isolate collision, unit circumcircle cover and adjacent-radius bounds")
 print("OMITTED: positive KKT, global optimality, unrestricted isolate relocation, Level I closure")
