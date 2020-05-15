import math
list = []
num = int(input('Co bao nhieu gia tri: '))
for n in range(num):
    gia_tri = input('Nhap gia tri: ')
    list.append(gia_tri)
a=print("Phan tu lon nhat :",max(list))
b=print("Phan tu nho nhat :",min(list))
