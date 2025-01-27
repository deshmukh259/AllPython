class Calc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __init__(self, a, b, c,v):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        self.check_type()
        print("adddd")
        return self.a + self.b + self.c

    def add(self):
        self.check_type()
        print("addccc")
        return self.a + self.b + self.c
    def mul(self):
        self.check_type()
        return self.a * self.b * self.c

    def div(self):
        self.check_type()
        return self.a / self.b / self.c

    def check_type(self):
        if not (type(self.a) == int and type(self.b) == int and type(self.c) == int):
            raise ValueError("invalid input for add")


if __name__ == "__main__":
    c= Calc(1,2,3,4)
    c.add()
