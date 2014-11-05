__author__ = 'T90'
__version__ = '1.0.0'



def rotate(strg, n):
	return strg[n:] + strg[:n]


def swap(i, j, c):
	c = list(c)
	c[i-1], c[j-1] = c[j-1], c[i-1]
	return ''.join(c)

count = 0
def val(s, t):
	global count
	count += 1
	print count, t + s


def six_steps(s, t = ''):
	val(s, t)
	val(swap(1, 2, s), t)
	val(swap(1, 3, s), t)
	val(swap(2, 3, s), t)
	val(rotate(s, 1), t)
	val(rotate(s, -1), t)


def permute(s):
	n = 4
	if len(s) == 3:
		six_steps(s)
	else:
		while n != len(s)+1:
			p = -1 * n
			print p
			sub, rest = s[p:], s[:p]
			for i in range(0, n):
				t = rotate(sub, i)
				six_steps(t[-3:], rest+t[: -3])
			n += 1


def main():
	a = "abcde"
	permute(a)


if __name__ == '__main__':
    main()