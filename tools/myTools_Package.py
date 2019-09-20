import os
import xlrd

class Function_Package:
	def __init__(self, dpath):
		self.dpath = dpath

def printName(names):
	for name in names:
		print(name.strip())

if __name__ == '__main__':
    names = ['张', '王', '李', '黄', '孙']
    printName(names)