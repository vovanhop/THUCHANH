import math;
x1=int(input('Nhap x1:'))
y1=int(input('nhap y1:'))
x2=int(input('Nhap x2:'))
y2=int(input('nhap y2:'))
d1=(x2-x1)*(x2-x1);
d2=(y2-y1)*(y2-y1);
res= math.sqrt(d1+d2)
print("distance between two points:",res);
