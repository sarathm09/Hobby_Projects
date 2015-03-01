import string


class Cipher():
	def __init__(self, text):
		self.text = text.upper()
		self.ans = ""
		self.alpha = list(string.ascii_uppercase)

	def caesar(self, decrypt=0):
		for i in self.text:
			if i != ' ':
				index = self.alpha.index(i)
				if decrypt == 0:
					index = (index + 3) % 26
				else:
					index = (index - 3) % 26
				self.ans += self.alpha[index]
			else:
				self.ans += i
		return self.ans

	def vignere(self, key, decrypt=0):
		key = key.upper()
		rep = abs(len(self.text) / len(key)) + 1
		key *= rep
		temp = 0
		for i in self.text:
			if decrypt == 0:
				if i != ' ':
					row = self.alpha.index(key[temp])
					col = self.alpha.index(i)
					self.ans += (self.alpha[row:] + self.alpha[:row])[col]
				else:
					self.ans += ' '
			else:
				if i != ' ':
					row = self.alpha.index(key[temp])
					col = (self.alpha[row:] + self.alpha[:row]).index(i)
					self.ans += self.alpha[col]
				else:
					self.ans += ' '
			temp += 1
		return self.ans

	def vernam(self, key, decrypt=0):
		key = key.upper()
		if len(self.text) != len(key):
			return "Error: Key and pText lengths don't match."
		temp = 0
		for i in self.text:
			if decrypt == 0:
				if i != ' ':
					row = self.alpha.index(key[temp])
					col = self.alpha.index(i)
					self.ans += (self.alpha[row:] + self.alpha[:row])[col]
				else:
					self.ans += ' '
			else:
				if i != ' ':
					row = self.alpha.index(key[temp])
					col = (self.alpha[row:] + self.alpha[:row]).index(i)
					self.ans += self.alpha[col]
				else:
					self.ans += ' '
			temp += 1
		return self.ans

	def playfair(self, key, decrypt=0):
		pmatrix = [[] for i in range(5)]
		key += ''.join(self.alpha)
		key = key.upper().replace("J", "I")
		row, col = 0, 0
		for i in key:
			curmat = ''.join([''.join(x) for x in pmatrix])
			if i not in curmat:
				if col == 5:
					row, col = row+1, 0
				if row == 5:
					break
				pmatrix[row].append(i)
				col += 1
		text, temp = "", self.text.replace("J", "I").replace(" ", "")
		if len(temp)%2 == 1:
			temp += 'X'
		for i in temp:
			text += i
			if (len(text)+1)%3 == 0:
				text += ","
		for i in text.split(",")[:-1]:
			row1, col1, row2, col2 = 0, -1, 0, -1
			for j in pmatrix:
				if i[0] in j:
					col1 = j.index(i[0])
				if i[1] in j:
					col2 = j.index(i[1])
				if col1 == -1:
					row1 += 1
				if col2 == -1:
					row2 += 1
			if row1 == row2:
				if decrypt == 0:
					col1, col2 = (col1+1)%5, (col2+1)%5
				else:
					col1, col2 = (col1-1)%5, (col2-1)%5
			elif col1 == col2:
				if decrypt == 0:
					row1, row2 = (row1+1)%5, (row2+1)%5
				else:
					row1, row2 = (row1-1)%5, (row2-1)%5
			else:
				col1, col2 = col2, col1
			self.ans += (pmatrix[row1][col1]+pmatrix[row2][col2])
		return self.ans



if __name__ == '__main__':
	print Cipher("MEET ME AFTER THE TOGA PARTY").caesar()
	print Cipher("PHHW PH DIWHU WKH WRJD SDUWB").caesar(1)
	print Cipher("we are discovered save yourself").vignere("deceptive")
	print Cipher("ZI EGX YMVGQZTKMY VEXI RWPVVINJ").vignere("deceptive", 1)
	print Cipher("MEET ME AFTER THE TOGA PARTY").vernam("abcdefghijklmnopqrstuvwxyzab")
	print Cipher("MFGW RK IODPD HWU LHAV MYQTZ").vernam("abcdefghijklmnopqrstuvwxyzab", 1)
	print Cipher("MY NAME IS ATUL").playfair("playfairexample")
	print Cipher("XFOLIXMKPVLR").playfair("playfairexample", 1)