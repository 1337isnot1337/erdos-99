#!/usr/bin/env python3
D=-2
t=8
rankP=4
old=(3,4,6,7)
def shadow(s,q):
    return D+2*s-3*q,(t-s)-(rankP-q),rankP-q
assert shadow(3,0)==(4,1,4)
assert shadow(3,1)==(1,2,3)
assert shadow(3,1)[0] < 4  # committed five-row k=2,p<=2 floor
w=[4,old[1],old[2],old[3]]
for i in range(1,4):
    w[i]=max(w[i],w[i-1]+1)
assert tuple(w)==(4,5,6,7)
def max_rank_loss(s):
    q=0
    for j,dj in enumerate(w,1):
        if dj<=s:q=j
    return q
assert [max_rank_loss(s) for s in range(1,5)]==[0,0,0,1]
assert shadow(4,0)==(6,0,4)
assert shadow(4,1)==(3,1,3)
print('PASS: k=4 D=-2 weights >= (4,5,6,7)')
