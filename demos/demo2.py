if __name__ == '__main__':

    d = {'a': '3'}
    try:
        v = [1, 2, 3]
        i = 0
        for i in len(v):
            v+=v[i]

        d['b'] = d['c']
        del d['c']
    except:
        print(3)

    print (d)

    print(float(str('10.0')))
    d = {
        'dd': None
    }
    r = {}
    r['dd'] = d['dd']
    print(r)
