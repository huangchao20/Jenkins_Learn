import os

def func01(path):
	if os.path.isdir(path):
		print('OK')
	else:
		print('Not OK')

def feib(n):
	a = 1
	b = 1
	if b < n:
		a, b = b, a + b
	return b

def func02(n):
	s = feib(n)
	if s < 10000:
		print('小数运算!!!~~~')
	else:
		print('超纲运算!!!~~~')

if __name__ == '__main__':
    path = 'G:\\黄大宝python\\py_function'
    func01(path)


# path = 'G:\\黄大宝python\\py_function'
# func01(path)
# path = 'G:\\黄大宝python\\py_function'
# func01(path)
# path = 'G:\\黄大宝python\\py_function'
# func01(path)