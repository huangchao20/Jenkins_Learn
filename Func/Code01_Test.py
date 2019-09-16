import os

def func01(path):
	if os.path.isdir(path):
		print('OK')
	else:
		print('Not OK')

if __name__ == '__main__':
    path = 'G:\\黄大宝python\\py_function'
    func01(path)


# path = 'G:\\黄大宝python\\py_function'
# func01(path)