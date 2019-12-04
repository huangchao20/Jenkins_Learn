import re

strs = 'www.runoob.com'
print(re.match(r'www', strs))
print(re.match(r'www', strs).span())
print(re.match(r'.*com', strs))

#--------------------------------------------------
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print('matchObj.group():', matchObj.group())
    print('matchObj.group(1):', matchObj.group(1))
    print('matchObj.group(2):', matchObj.group(2))
else:
    print(None)
#________________________________________________
print(re.search(r'com', strs).span())
print(re.search(r'www', strs).span())
print(re.search(r'com', strs))
print(re.search(r'www', strs))

#________________________________________________
searchObj = re.search(r'(.*?) are(.*?).*', line,  re.M | re.I)
print('searchObj.group():', searchObj.group())
print('searchObj.group(1):', searchObj.group(1))
print('searchObj.group(2):', searchObj.group(2))

phone = '028-1234-7891  #解释一个电话号码'
num = re.sub('#.*$', '', phone)
# num = re.sub('#.*$', '', phone)
num2 = re.sub('\D', '', phone)
print(num)
print(num2)
