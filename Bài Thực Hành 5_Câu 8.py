def Sequential_Search(ch, n, x):
    for i in range(n):
        if (ch[i] == x):
            return i
    return -1
ch=[]
n =int(input('So item: '))
for k in range(n):
    item=input('Nhap item: ')
    ch.append(item)
x =input('Nhap vao ten item can tim: ')
n= len(ch)
result = Sequential_Search(ch, n, x)
if (result == -1):
    print("item khong có trong mang")
else:
    print("item co trong mang", ' vi tri:',result)