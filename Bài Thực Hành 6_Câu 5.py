class daochuoi(object):
    def __init__(self,s):
        self.ch=s
    def dao(self):
        return ' '.join(reversed(s.split()))
s=input('Nhap chuoi:')
Day=daochuoi(s)
print('Chuoi sau khi dao la:',Day.dao())