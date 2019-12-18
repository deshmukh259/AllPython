if __name__ == "__main__":
    # for v in range(int(int(input()))):
    #     c[v] = input()
    # x = 0
    #z = ['1415926535 8979323846 35',
    #     '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196 104683731294243150']
    z = []
    coun = int(input())
    if coun <1 and coun >100:
        exit(0)
    for zz in range(coun):
        z.append(input())

    x = 0
    len1 = len(z)
    while x < (len1):

        bb = z[x].split(' ')
        x += 1
        a = bb[0];
        if(len(a) <1 and len(a)>100):
            exit(0)

        b = bb[1];
        if(len(b) <1 and len(b)>100):
            exit(0)
        n = int(float(bb[2]));
        if n< 1 and (1<<100)+1 > n:
            exit(0)
        # q = int(n / 7);
        q = n
        c = '';
        i = 0

        for i in range(q - 1):
            if len(c) < (n + 1):
                c = a + b;
                a = b;
                b = c;

        # print(c)
        n_ = n - 1

        print(c[n_])
