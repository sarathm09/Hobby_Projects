__author__ = 'T90'
__version__ = '1.0.0'


def read_from_file():
	f = open("22names.txt")
	data = f.read()
	list = data.split('","')
	list.sort()
	return list


def process_list(l):
	n = 0
	s = 0
	for name in l:
		n += 1
		ascii = sum([ord(c)-ord('A')+1 for c in str(name)])
		ns = ascii * n
		s += ns
		if n == 938:
			print name,ns,ascii
	return s


def main():
	print process_list(read_from_file())


main()