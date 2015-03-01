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


if __name__ == '__main__':
	print Cipher("we are discovered save yourself").vignere("deceptive")
	print Cipher("ZI EGX YMVGQZTKMY VEXI RWPVVINJ").vignere("deceptive", 1)
	print Cipher("MEET ME AFTER THE TOGA PARTY").caesar()
	print Cipher("PHHW PH DIWHU WKH WRJD SDUWB").caesar(1)