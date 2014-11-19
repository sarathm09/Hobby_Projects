__author__ = 'T90'
__version__ = '1.0.0'

import re
import Image

i = Image.open("l7.bmp")
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))