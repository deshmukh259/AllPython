

def c(x):
    return x%3==0
def d(i,x):
    return {i:x}

if __name__ == "__main__":

    v = [d(i,x) for i,x in enumerate(100) if c(x)]
    print(v)
    print(dir(v))
