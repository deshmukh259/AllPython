def hello():
    print("hello ")


if __name__ == "__main__":
    list = [4, 3]
    print(list)
    list.append(33)
    print(list)
    hello()
    print(type(2.3))
    print(id(print("")))
    print(2 + 5j)
    s = "ABCDefghwert"
    print(id(1))
    b = bytes(list)
    list.append(55)
    print(b[-1])
    print("-----------")
    for i in list:
        print(i)
    list.reverse()
    print(list)
    list.sort()
    print(len(list))
    i = range(10)
    print(2 ** 3 ** 2 ** 1)
    print('abcf\' fd\"f')
    b = 250
    b //= 2
    print(b)
    s = {100, 'abcd', 'abcd ', 0}
    print("Hi " * 5)
    print(2 == 2 == 2 == 3)
    print(-1 << 3)
    print(300 if 22 == 22 else 22)
    print(125 is b)
    print(100 in s)
    print(7.0 // 2.1)
    print("Enter value:")
    vv = input()
    print(type(vv))
    print(vv)
