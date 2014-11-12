def pali(st):
    return st == st[::-1]


def process(s):
    op = 0
    n = len(s)-1
    while not pali(s):
        while s[n] != 'a':
            s[n] = chr(ord(s[n])-1)
            op += 1
            if pali(s):
                break
        n -= 1
    print op
                       

def main():
    n = input()
    for i in xrange(0,n):
        process(list(raw_input()))



main()
