def func01(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print("%s*%s=%s" % (j, i, i * j), end='\t')
		print(end='\n')

if __name__ == '__main__':
    n = 9
    func01(n)
    print('')


