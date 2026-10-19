from fractions import Fraction as F
from itertools import combinations
m=7
L=14
eps=F(1,10*L**4)
t=F(1,100*L**3)
def pt(i,j):
    # Physical coordinates represented by (x,q) for (x,sqrt(3)*q).
    x=F(i)+F(j,7)
    q=F(4*j,7)
    if 1<=i<=6 and 1<=j<=6:
        lam=F((7-i)*(7-j))*(1+eps*(7-i))
        x-=t*lam*F(8,7)
        q-=t*lam*F(4,7)
    return x,q
labels=[(i,j) for i in range(8) for j in range(8) if (j==7 or i==7 or (1<=i<=6 and 1<=j<=6))]
assert len(labels)==51
pairs=[]
for a,b in combinations(labels,2):
    x1,q1=pt(*a); x2,q2=pt(*b)
    d=(x1-x2)**2+3*(q1-q2)**2
    pairs.append((a,b,d))
lo=min(d for _,_,d in pairs); hi=max(d for _,_,d in pairs)
assert len(pairs)==1275 and lo>=1 and hi==84 and hi<=112
moved=[p for p in pairs if ((1<=p[0][0]<=6 and 1<=p[0][1]<=6) or (1<=p[1][0]<=6 and 1<=p[1][1]<=6))]
assert len(moved)==1170 and min(d for _,_,d in moved)>1
maxpairs=[(a,b,d) for a,b,d in pairs if d==hi]
print({'labels':len(labels),'pairs':len(pairs),'min_squared_distance':str(lo),'max_squared_distance':str(hi),'max_pairs':maxpairs,'moved_pair_count':len(moved),'min_moved_pair_squared_distance':str(min(d for _,_,d in moved)),'all_upper_le_original_112':True})
