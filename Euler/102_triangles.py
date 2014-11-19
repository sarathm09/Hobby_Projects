__author__ = 'T90'
__version__ = '1.0.0'

a, b, c = [], [], []


def readndsplit():
	f = open("102_triangles.txt")
	complete = f.read()
	triangles = complete.split("\n")
	for tr in triangles:
		vals = tr.split(",")
		a.append(int(vals[0]))
		a.append(int(vals[1]))
		b.append(int(vals[2]))
		b.append(int(vals[3]))
		c.append(int(vals[4]))
		c.append(int(vals[5]))


def area(x1, y1, x2, y2, x3=0, y3=0):
	return 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))


def check(n):
	tarea = area(a[n], a[n + 1], b[n], b[n + 1], c[n], c[n + 1])
	area_sum = area(a[n], a[n + 1], b[n], b[n + 1]) + area(b[n], b[n + 1], c[n], c[n + 1]) + area(a[n], a[n + 1], c[n],
																								c[n + 1])
	if tarea == area_sum:
		return True
	else:
		return False


def main():
	n = 0
	readndsplit()
	for i in xrange(0, len(a), 2):
		if check(i):
			n += 1
	print n

main()
