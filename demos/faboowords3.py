if __name__ == "__main__":
    # for v in range(int(int(input()))):
    #     c[v] = input()
    # x = 0
    z = ['1415926535 8979323846 35',
         '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196 104683731294243150']
    # z = []
    # coun = int(input())
    # if coun < 1 and coun > 100:
    #     exit(0)
    # for zz in range(coun):
    #     z.append(input())

    x = 0
    len1 = len(z)
    while x < (len1):
        bb = z[x].split(' ')
        x += 1
        a = bb[0];
        b = bb[1];
        n = int(float(bb[2]));
        le = len(a)
        f = None
        n/2
        if (int(n / le)) % 2 == 0:
            f = b
        else:
            f = a
        nr = 0
        cv = 0
        bb = 0
        # while nr < n:
        #     nr = nr * le
        pos = int(n - (int(n / le) * le))
        print(f[pos - 1])
