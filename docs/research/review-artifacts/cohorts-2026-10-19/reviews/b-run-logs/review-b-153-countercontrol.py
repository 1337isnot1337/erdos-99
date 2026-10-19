from fractions import Fraction as F
# Unit direction v=(1,0), moving p=(0,0), fixed q=(1,0).
v=(F(1),F(0)); p=(F(0),F(0)); q=(F(1),F(0)); s=F(1,2)
wrong=(q[0]-p[0],q[1]-p[1]) # literal predecessor moving-to-fixed orientation
right=(p[0]-q[0],p[1]-q[1]) # corrected fixed-to-moving orientation
wrong_floor=max(F(0),-2*(wrong[0]*v[0]+wrong[1]*v[1]))
right_floor=max(F(0),-2*(right[0]*v[0]+right[1]*v[1]))
new=p[0]+s*v[0]-q[0],p[1]+s*v[1]-q[1]
d2=new[0]*new[0]+new[1]*new[1]
assert wrong_floor == 0 and s > wrong_floor and d2 == F(1,4) < 1
assert right_floor == 2 and s <= right_floor
# Reverse orientation: moving p=(1,0) away from fixed q=(0,0) with v=(1,0).
p2=(F(1),F(0)); q2=(F(0),F(0)); r2=(p2[0]-q2[0],p2[1]-q2[1])
reverse_floor=max(F(0),-2*(r2[0]*v[0]+r2[1]*v[1]))
new2=p2[0]+s*v[0]-q2[0],p2[1]+s*v[1]-q2[1]
d2away=new2[0]*new2[0]+new2[1]*new2[1]
assert reverse_floor == 0 and d2away == F(9,4) > 1
print({'wrong_orientation_floor':str(wrong_floor),'actual_new_distance_squared':str(d2),'corrected_floor':str(right_floor),'reversed_contact_release_floor':str(reverse_floor),'away_distance_squared':str(d2away),'result':'PASS'})
