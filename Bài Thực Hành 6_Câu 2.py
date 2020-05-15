class Hinhchunhat(object):
    def __init__(self, l, w):
       self.dai = l
       self.rong = w
    def area(self):
       return self.dai*self.rong
l=int(input('Nhập chieu dai:'))
w=int(input('Nhập chieu rong:'))
aHinhchunhat = Hinhchunhat(l,w)
print ('Dien tich hinh chu nhat la:',aHinhchunhat.area())