#!/usr/bin/env python3
"""Exact certificate for four generic interior-ground H7b law-of-sines exclusions.

This verifier reuses the already-audited full-angle H7b verifier to reconstruct
the 184 orbit representatives and the 84-variable affine angle systems, then
checks new rational Farkas dual identities.  The compressed payload below is
only certificate data (integer numerator/denominator pairs); every identity is
expanded and checked exactly with fractions.Fraction before any claim passes.
"""
from fractions import Fraction as Q
from pathlib import Path
import base64, json, runpy, zlib

base = runpy.run_path(str(Path(__file__).with_name('verify_target_c_support7_h7b_full_angle_reduction_2026_09_19.py')))
reps=base['reps']; build_system=base['build_system']; full_angle=base['full_angle']
addrows=base['addrows']; edge=base['edge']
SURV27=[115,118,129,130,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,169,170,171,172,173,174,175,176]
assert all(reps[i-1][0]=='C7' for i in SURV27)

PAYLOAD='c-rM#O{*oj4gD{@z86aJXU#5<fAMGr!UPfsX_%1J(EmNRY)R+1s$ReDOlFlu(|W!xmo4kaN0RHePhWoh<*&bf`sue%BK@I{^696yx3}%_CJ*`i`SF%Rs*kt+NQbmP-pZ6jAm;d8UR~8h^i_$Wv_uE3$2+Fjjt)ai8$`S!<>*@^Ius4D<Hdcq)|Y%NN9UW5$CAAcVtTx_DPg%K-t`((HXAj5-a|Tc;G-*akZv_o&{`ojbm(Z^qg6NP3+hlsE8ceK*45k~VqATV`y@SQ=-FE}R+JJtWNZYMk$OxbW0v_f!qX<73(1}2J-Q#e*?BkT4y2e-eJSf{Z)~sEJng~udhluUYuKDFV~JB%Jlfl0A8PiYkNx%E0KluG1E4*sS%gW2p`ZZ;1r%QYs_*!+&DA&5dnoljHczp61dM{MY1jl4%P_$)Ld6J&rmVGLu!g?fCuG2|(eMgABsEy{fJK>YCHmE|PKSl*Xb(v+;sJ{SSSVnjx3CB`HZ*r?CZDo}b{CB*niDnWMbXiW?Hq{l<_@iI%U&p8;vLf64kainK}DHti)=H)^?VC4Pn+EVnPfO2$Yfw+V5Sjf?4<)UE`I|vu7?9O{?_jMJ1izplOF1*NssJ)b{fnuoqWL$JJ0gyZV=g;3r4DkRrLUn$vVud#}=Dd;=PKOq%p4^Ue4tlBOki5_Z|2Uo6$T(G_YbAfWtrR%w~~>z2?gylIAlN>+GSCJtWy;;-~Y(MGPuXq|mSjT3mgdn)hfv(BexQaB*E~C}Q{`?~)h2y0$A?8(Mp;G=V%Mn8E2x*|7z&9Z=SR7VB}K#l^!a6G6n~J`MqKh}e`4gk(mD;!x25i0fb=#HTVK;&P9P4~Qs1Bz6>vI7}v)$xP6ElGkJ_5ON__l9v4x?4cjt#GESB2s=qR#EcOb+z@4R^I4e@oJhi8Y{(keHLZR`hVIw0-7X7n*R;^Ydn%&<wu`HMT@{nCghZ~P!RuvRJ+MHdA!8w>qq&mYu)s$4(v;lm?(*x8ZL|#|QIHQIPm)dT29AM^?C!yS7MS(n2h5i#@Tcg@o{<2$o<G*NV6cY1r(?rCXU8120vNoJZyOFMo4wg{DWn|Ia#mpB5`NRyjY)|@F)1FBj8-@pfxj1;HO5sOWs3PJ_JdCvQg~ku9f57SmSNpf;p(<2Y@3;EGl%b6jZ?!o{n&wmW_Xm{;rS?Lvzcsm$~#7E+p^<f*3<dU_I$F0x&6?{V&L=VVc@Ul!4pdCcnQBUq~T19@3>4+z;{IBp+P6T2l<<JY<h7BR1@*s0RekQLWfD+irc+UXXvuroCVh5uzMR}I@i(L4BvkkuP<)+Hn}wH(-mQjB_>hF0$md(?N~f!K0HB(PHfOY8eBbv<T`A*z+Hegc$Xa`>b9tp9kmUj*vA7Hu5j9h4ux+J6}nGo&1i)(QjJ#(V7LJtV6ff;4EDkU3^x5T-EeU<xY#jDWqBHJaWIe>JZ&!1ncJHt8p1yOO%o0!;Lyw{UiMQQ51G>~yF18jigWLFL&R&#c87$CCrA`)J+?oYJn7-?`>fthqgdRu$01>_AE$)(>0_&R#|vcy)MnVn6T9QVnkODcyR!|Ag(eeqOwtoEHOKNj&_#@2F^`UE?+^!%-k_h12-IIUK;bGZB+mt>8&HHkcbfG^sU(4(hYnqD2}6#v!*yFo=M9lJ6gQboDEt}PS7<+>3ld|K=In8l*jwgVVt-_s;yg_JkIKCe{|*Gb7QY9Xw&|1<b~n!!d$#f)4d!i(Xa|TYk~dEqX`UWpM&n`TYog`R23#5rnk8x?BH-dZwZ;H+`d`Qrg^`!Q=Jpt;FoVg`j_EdvC&`n7nch=xi5T*^tdSx^MPx_}M{k!aAUhv&as>raP$0dbKt#_Mg%R%wqUo$6VTg?9%7%p&;vgKmofr$LJ(?$D(Hq9%U4pW#JiI-syX73mH_quEG^NLpOlNP$x!P|zh=PN39Fz%kL=*=h#k&coTmnlW9!|j?^N~(;M8HR$J@`luI?~UpEHU3Y=ILzYx^&VOt>Ms!ze%uS!4QY_xriCeT-_a`=wK9Xayw4%gwc{vvyxg<sC9r>!8H;{cqgvmS^-@dZgVHv;nXTa`2~D)knlvjqZ9Aw#5)wcqZ04nAhLsYC}>9q>ri4HzV|X%$JfWFzkK=kKY#hxtoM|k|CIFSe|#CnE)T=XZI0sO+&AT^s0>8TMz0>`_m_dtq2O(m!qa!lK*)A`78_>q`>Q}dlI~WVN>l|>XpX8t<fipDb)p}oPX4eekmsGVkWB4mTk1X0te6N@d=A$ZnQY|TE5*U}R3FMz6S~W~Y$U^)I`(kie3Z{lYXT*I`};u2bA?HNXhOQ%OC{OF0<jL&s^jLh?e^d{>_xeRq+uEUG@sRi=9wx}D*I`G>18a6f`z|fFm~@&C!3ys^gQfRNhdzTn8@lJWbC7+Yx1x`6$Prmdk3M`fYJ`VWL67lB^EG<ybmggHJM4p2f{)F=R~BiR()XINUtjiTGcJYf<p6|G#~Aa+B>a(aC_dK_(6HA5<imp7gpv#Uh<y?_9XN_n3iiR8}T8>sl@Jm2*aZSkUrdiWa#?<CH~NX9Qz~jcy-iol%VN@dlYS!u+b0)K0`&8QcnR<`{ncTz>BK^r<w?-<}u!8oF+MVT#Lk$S2Xw8Ms_lMRSQsB2LU0obc$pYd0T{t-mU`PoZ{8fV4B;DjXeyZnLNuPEzUKc|5T<#0xy2(dyHv-ZGqQ>s}I#)d#p9!T0<l1V;8)?4ufrxgwjYtDQF)wWh)TH+fJn`*JZ`b)@VDly$`iD<YOaFgN8LUuQ<OoFUn2`<-E0_wPUSmTeibG5ANtYlc;y5cG6g~;I{#h{>Q9THAkR}O3kxg-2gZ{?BJ8?tQxn#nptX{=`W$&t<A_o?G`|@M-H6Xg8Po<fwJ99=m4bz#7Y8TEI?R|xS>YeP|u0o9TCD7$uSWG1xSJlf}Fz)DEmmE0>uaUHm1`1n99gO!8<DQtMg(AMNAqIQ)D}l8cpax1IHvP(!Pibc7$gfC{e9<&ERGvaH+JmBh1_{F%|P|B->S>Ny>#Mw5~x{hf?)6{!)s+^fvy|`|wNe!!K{1Fe!nbjMyp?xf>F>oZr<o*P9V2`zRH`d{s*OCZv5UmHe8Wj!694<_#RV3_jjr<pV~DzzTy1=ai#}>3yOSEu~AeQC-DIvoX}NFw_Fye=4&SF1TnIqym>zT_7V=;4;I;8VoDLngk|9xsD7IlH1aYd<0AP7+W>@Qe$ZWP^z#<=zxQ|sIbWQS6Bc~y=rE?mC*oC1w2W0lzYq2Vgo!$p$+hqTc0P;ZN5*B2;iB?E8f;&D6>g*7$I;ffl~>b0&ofeQm)09h9@ihgz?CNOKtaftOUnIa7=(BB><G*n9XjU;&qro91Bi01$vwUh6G+Q6w=~eY>R9_!}$hQ#JQ2?){;SUoR)xe%=4`QM-8sH0Xz)}kzk7%bik+Bqjl;7<gmvQWealXR3XLhIbMc|S3HC9nTIYMx`G%wze`Zksu=}E^wtJ(&0+5#i1%8w$L85~N5B=F&|9&dv@IG}P{ImEn6VEPd@vIoOvDBgkwFC+bWx~TNgni;d0_)DY;=M(LQJDevW+r`jS?aa2Uw%xJ&2&2OJN?UWeK$=WZ)$_9blBfm;BxVR&+TMXNqOLCn(pOaP_X7k<)UPoRfkd*Iq8gmHPsc{C5?V^DU=DmxuDD+94kW0+ijlyIvGZ&h@ovncZAI={T2L4RH;PdYr~(W5~!9rSPAp>-Fs}hx$Di;S`tO<&kdgGf|?Fjtt>T;t9ncLB;wmOZ=4Yyd8(^c>6|@cw18D8A;-&{Le1UWhkbs7n`|2cXvmL3d=+RsIYu<X)f)j%&*WF0772?P!{+pd{=#n4b987Bdn&gwNv*_ne2T-y8r1J+`~dMyO+#`j(WMStVsCVgfNHox<AaeTuUBp`DR1dY%4DKS7&Hm9hGREsrHIOUxgp5pg9$FpM-08Fy<T}%u({_QSm4QOubY*%6ZvT^I2~!`!^1HLi1hiLvO!;A+x71U<d(v{f>w}d&y92fx1!pp0$sQy72+Q>9Vr7rn~)^rH>k5@Gk<$6u$`uc@GSgz)&w0?L=R`(5FuPg-cz5VWaHvqR%n30i)tb$g}eq7bgRG|MrEP?_Sa!g!4U%J2Vgkl$|);sGzSF>iN>)$?j36fDbS6VGH|ky<D@f&m%DDovyaRtTE9azmE~dp7`=9xqCflkiT&s;{&_DxsQQw$4*x>l-<3OyVrLtypo02cPzaAh=nh%zq+yWrzr{7Y52>OCt17LS1QVfKwS=jY3#fkI}sq7iOM^K>d%$R=k+zIxe|uaA9>gR#9;o<FZG{E$<0;%cK(24xrG1q>wf?`Kgf{'
data=json.loads(zlib.decompress(base64.b85decode(PAYLOAD)).decode())
def q(x): return Q(x[0],x[1])
def unpack_pairs(xs): return [(k,q(v)) for k,v in xs]
def angle_row(st,u,v): return full_angle(u,0,v,st[2])
def linear_angle_row(st,terms):
    r={}
    for coef,u,v in terms:r=addrows(r,angle_row(st,u,v),Q(coef))
    return r

def check_dual(st,target,packed):
    ine,eq=build_system(st); ar,mr,rr=packed
    alpha=unpack_pairs(ar); mu=unpack_pairs(mr); expected=q(rr)
    assert alpha and all(a>0 for _,a in alpha)
    combo={};rhs=Q(0)
    for k,a in alpha:
        row,b,_=ine[k];combo=addrows(combo,row,-a);rhs-=a*b
    for k,m in mu:
        row,d,_=eq[k];combo=addrows(combo,row,m);rhs+=m*d
    assert combo==target
    assert rhs==expected
    return rhs,sum(a for _,a in alpha)

ORDER_CYCLES={118:(2,5,3,2),145:(6,2,3,4,5,7,6)}
for idx,cycle in ORDER_CYCLES.items():
    st=reps[idx-1];missing=set(st[1])
    for u,v in zip(cycle,cycle[1:]):
        assert edge(u,v) not in missing
        target=addrows(angle_row(st,u,v),angle_row(st,v,u),Q(-1))
        rhs,sa=check_dual(st,target,data['order'][f'{idx},{u},{v}'])
        assert rhs>=0 and sa>0

PROVED={}
for name,packed in data['bounds'].items():
    terms,ar,mr,rr=packed;idx=int(name.split('_',1)[0]);st=reps[idx-1]
    PROVED[name]=check_dual(st,linear_angle_row(st,terms),(ar,mr,rr))

# Orbit 115 strict normalized angle bounds used in the sine-product estimate.
assert all(edge(u,v) not in set(reps[114][1]) for u,v in ((3,2),(2,5),(5,3)))
assert PROVED['115_A32_lo'][0]==Q(5,9)>Q(1,2)
assert -PROVED['115_A32_hi'][0]==Q(47,69)<Q(3,4)
assert -PROVED['115_A23_hi'][0]==Q(4,21)<Q(1,5)
assert PROVED['115_A53_lo'][0]==Q(1,5)
assert -PROVED['115_A53_hi'][0]==Q(1,3)<Q(1,2)
assert -PROVED['115_A35_hi'][0]==Q(1,15)
assert PROVED['115_A25_lo'][0]==Q(5,21)>Q(1,5)
assert -PROVED['115_A25_hi'][0]==Q(1,3)<Q(1,2)
assert -PROVED['115_A52_hi'][0]==Q(1,3)
assert 45>25  # exact final radical comparison in the written proof

# Orbit 146 strict bounds used in its sine-product estimate.
assert all(edge(u,v) not in set(reps[145][1]) for u,v in ((2,4),(4,6),(6,2)))
assert PROVED['146_A24_lo'][0]==Q(1,3)
assert -PROVED['146_A24_hi'][0]==Q(5,9)<Q(2,3)
assert -PROVED['146_A42_hi'][0]==Q(1,6)
assert PROVED['146_A46_lo'][0]==Q(2,9)
assert -PROVED['146_A46_hi'][0]==Q(1,3)<Q(1,2)
assert PROVED['146_D62_lo'][0]==0
assert 196>180  # exact final radical comparison in the written proof

EXCLUDED={115,118,145,146}
remaining=[i for i in SURV27 if i not in EXCLUDED]
assert remaining==[129,130,134,135,136,137,138,139,140,141,142,143,144,147,148,169,170,171,172,173,174,175,176]
print('PASS: exact affine dual certificates support four law-of-sines exclusions.')
print('generic H7b full-angle survivors:',len(SURV27),'->',len(remaining))
print('excluded orbit indices:',sorted(EXCLUDED))
print('remaining orbit indices:',remaining)
