def getV():
    yield 1
    yield 2
    yield 3


def getB():
    yield v()


def v():
    c = 1
    while (c < 30000000000000):
        c += 1
        yield c
if __name__ == "__main__":
    line_list = ['  line 1\n', 'line 2  \n']
    #stripped_iter = (line.strip() for line in line_list)
    vv = [(line.strip() for line in line_list )]
    for l in vv:
        print("xx"+str(l))
    #print(stripped_iter)
    #print(type(stripped_iter))



def v():
    v = getB()
    c = 4
    while (c < 3000):
        c += 1
        print(next(v))

    print("00000000000000000000000")
    print(next(v))
