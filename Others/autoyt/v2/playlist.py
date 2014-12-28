def getSafeFilename(name):
	path = list(name)
	path[0] = path[0].upper()
	for i in xrange(len(name) - 1):
		if not name[i].isalnum():
			path[i + 1] = name[i + 1].upper()
		else:
			path[i + 1] = name[i + 1].lower()
	return "".join(x for x in path if x.isalnum())


print getSafeFilename("my naMe is abc")
print getSafeFilename("hello $123 ny & xy")