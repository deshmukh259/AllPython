from collections import namedtuple

if __name__ == '__main__':
    a = namedtuple('stu', 'name, age')
    v = a('ap',24)

    print (v)
    #print(v('name'))
