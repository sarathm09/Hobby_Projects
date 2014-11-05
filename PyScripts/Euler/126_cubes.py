def Cubes(x, y, z, n):
    return 2 * (x * y + y * z + x * z ) + 4* (x + y + z + n - 2) * (n - 1);

limit = 30000;
count = [0 for i in range(0, limit+1)]
z = 1
while Cubes(z, z, z, 1) <= limit:
	y = z
	while Cubes(z, y, z, 1) <= limit:
		x = y
		while Cubes(z, y, x, 1) <= limit:
			n = 1 
			while Cubes(z, y, x, n) <= limit:
				count[Cubes(z, y, x, n)] += 1
			n += 1
		x += 1
	y += 1
z += 1

print count