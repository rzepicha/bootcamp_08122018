
import struct

with open(r'C:\Program Files (x86)\Microsoft Office\Stationery\1033\CURRENCY.GIF','rb') as f:
    img = f.read()

#gif header opisujący rozpisanie gifa: http://www.onicos.com/staff/iz/formats/gif.html
#https://docs.python.org/3.7/library/struct.html
print(struct.unpack('<HH', img[6:10]))


