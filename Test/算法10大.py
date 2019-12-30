def test1(n):
    for i in range(n):
        if i > 5:
            # print(i)
            break
    else:
        print('This is OK??')
    

def test11(n):
    for i in range(n):
        if i > 10:
            print(i)
            # break
    else:
        print(i, '老子是你爹')
   
        
#一颗星(*)
def test2(*args):
    s = 0
    for i in args:
        s += i
    print(s)

#两颗星(**)
def test21(name, age, gender='男', *args, **kwargs):
    print('姓名: %s 年纪:%s 性别:%s' % (name, age, gender))
    print(args)
    print(kwargs)
    
def test3(lis):
    result = list()
    for i in lis:
        result.append(i ** i)
        print(result)

def test31(lis):
    result = []
    result.append(i ** i for i in lis)
    print(result[0])
        
if __name__ == '__main__':
    # test1(6)
    
    # test11(11)
    
    # test2(2, 5, 7, 3, 1)
    
    # test21(3, 4, 5, 110, 256, 英语=6, 数学=7)
    
    # a = (1, 2, 3)
    # print(a)
    # print(*a)
    # #1 2 3
    # b = [4, 5, 6]
    # print(b)
    # print(*b)
    #
    # c = {'name': 'xufive', 'age': 51}
    # print(c)
    # print(*c)
    
    print('你是一个傻逼' if 2 < 3 else '傻逼都是你')
    
    lis = [4, 5, 6, 7]
    test31(lis)
    pass