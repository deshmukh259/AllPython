from functools import reduce

if __name__ == "__main__":
    print("hello")
    v = lambda: 4*66
    print(v())
    l = [1,3,44,55,666,777,333,55,555]
    print(tuple(filter(lambda x: x<333,l)))
