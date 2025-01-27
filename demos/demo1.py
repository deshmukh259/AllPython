import re


class a:
    s = 55

    def __init__(self, s):
        self.s = s
def test(key = None ):
    print(key)


def fun1(a):
    ee = "abc"
    dd = "s"
    print(type(dd))
    dd = 4.5e0
    print(type(dd))
    dd = 3.03j
    print(dd + 1)
    print(type(dd))
    b = a(33)
    c = a(332)
    if (b.s > c.s):
        print(b.s)

    print('-------------')
    print(ee[1])
    print(ee[0])
    print(ee[0])
    print("x")
    print(type(x))
    # print(x + 4)

    d = "abcdxyz   "
    print(d)
    print(d[3:5])
    print(d.strip())
    print('-----------')
    print(len(d))
    print(d.upper())
    print(d.split("d"))

    # x = input()
    # print(x)
    x = 2.0 / 2.5
    print(x)
    print(x is x)
    x = ['a', 'b', 'c', 'd']
    print('---------------')
    for a in x:
        print(a)

    x.append('w')
    print(x)
    print(len(x))
    x.insert(1, 'aa')
    x = {'a', 'b', 'c', 'd', 'd'}
    print(x)

    x = {"abcd": "abcd"}
    print(x)
    print(x["abcd"])
    x["abcd"] = "xyz"
    print(x)
    x=dict(abc="xyzz")
    print(x)
    for x in range(1,4):
        print(x)


def get_op(qStr, qfield):
    match = re.search(r'\b'+re.escape(qfield)+'\[', str(qStr))
    return str(qStr)[match.end():match.end() + 2]

if __name__ == "__main__":
    #test()
    #fun1(a())
    if "" == "":
        print("ss")
    p={'1abcd':'xyz',
       'abcd[in]':'abcd,xyz'}
    print(str(p))
    #match = re.search(r'\babcd\[\b', str(p))
    #print(match)
    #print(match.end())
    #print(str(p)[match.end():match.end()+2])
    #print(re.search("abcd?", p))
    #print(p['abcd?'])
    print(get_op(p,'abcd'))

