import os

def printInfo(filename):
	if os.path.isdir(filename):
		print(os.listdir(filename))
	elif os.path.isfile(filename):
		with open(filename) as fs:
			for f in fs.readlines():
				print(f, end='')
	else:
		print('你是逗逼嘛，乱整')



if __name__ == '__main__':
	fList = ['G:\\黄大宝python\\2018', 'G:\\黄大宝python\\2018\workspace\\PyTrade_fbap\\T0825000003_B0101.py', 'G:\\黄大宝python\\2018\workspace\\PyTrade_f']
	for filename in fList:
		printInfo(filename)
		print('---------------filename---------------')