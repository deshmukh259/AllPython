class Calc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        self.check_type()
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
