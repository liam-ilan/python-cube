import os;import math;from time import sleep;
mS=lambda w,h,c: [[c] * w for _ in range(h)];
cl= lambda: os.system('clear || cls');p='\n';
rS=lambda s: cl() or print(p.join([''.join(r)
for r in s])); dL=lambda sc, p1, p2, c, co:((
dx:=p2[0]-p1[0])or True)and((dy:=p2[1]-p1[1])
or True)and((st:=max(abs(dx),abs(dy)))or True
)and((dx:=dx / st)or True)and((dy := dy / st)
or True)and((x:=p1[0])or True)and ((y:=p1[1])
or (True)) and ([((sc[int(y)].insert( int(x),
'\033[0;'+str(co+30)+';40m'+c+'\033[0;0m'))or
True) and((sc[int(y)].pop(int(x)+1)) or True)
and((x:=x+dx)or True)and((y:=y+dy)or True)for
i in range(0, int(st) + 1)] or True); eC='█';
bc = ' '; size = os.get_terminal_size();':D';
w = size.columns; h = size.lines;l=lambda t:(
(sc := mS(w,h,bc)) or True)and((c:=[int(w/2),
int(h/2)]) or True) and ((r:=10)or True)and((
s:=2.5) or True)and((d:=10)or True)and((p1:=[
math.cos(t)*r+c[0],math.sin(t)*r/s+d/2+c[1]])
or True)and((p2:=[math.cos(t+math.pi/2)*r+c[0
],math.sin(t+math.pi/2)*r/s+d/2+c[1]])or True
) and ((p3:=[math.cos(t+math.pi)*r+c[0],math.
sin(t + math.pi) * r/s+d/2+c[1]])or True)and(
(p4:=[math.cos(t+3*math.pi/2)*r+c[0],math.sin
(t+3*math.pi/2)*r/s+d/2+c[1]])or True)and((p5
:= p1.copy())or True) and ((p6:=p2.copy()) or
True) and ((p7:= p3.copy())or True) and((p8:=
p4.copy()) or True) and(p5.append(p5[1]-d) or
True)and(p5.pop(1)or True)and(p6.append(p6[1]
-d)or True)and(p6.pop(1)or True)and(p7.append
(p7[1]-d)or True)and(p7.pop(1)or True)and(p8.
append(p8[1 ] - d) or True) and (p8.pop(1) or
True) and(dL(sc,p1,p2,eC,1)or True)and(dL(sc,
p2,p3,eC,2)or True) and (dL(sc,p3,p4,eC,3) or
True) and (dL(sc,p4,p1,eC,4)or True)and(dL(sc
,p1,p5,eC,1)or True)and (dL(sc,p2,p6,eC,2) or
True) and (dL(sc,p3,p7,eC,3)or True) and (dL(
sc,p4,p8,eC,4)or True)and(dL(sc,p5,p6,eC,1)or
True)and(dL(sc,p6,p7,eC,2) or True)and(dL(sc,
p7,p8,eC,3)or True) and (dL(sc,p8,p5,eC,4) or
True)and(sleep(0.15)or True)and(rS(sc)or True
)and(l(t+0.1)or True);l(0);'''...............
..................Liam Ilan..................
..........................................'''