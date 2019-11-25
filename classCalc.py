class Data:
    __d=90
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        print("a:" + str(self.a) + " b:" + str(self.b) + " c:" + str(self.c))

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def setC(self, c):
        self.c = c

    def setABC(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def v(cls):
        print(cls.__d)

class Calcution(Data):

    def sum(self):
        self.display()
        print("sum :" + str(self.a + self.b + self.c))

    def diff(self):
        self.display()
        print("diff :" + str(self.a - self.b - self.c))

    def mul(self):
        """ mul function"""
        self.display()
        print("mul :" + str(self.a * self.b * self.c))
        return self.a * self.b * self.c


if __name__ == "__main__":
    print ("Employee.__doc__:", Calcution.__doc__)
    print ("Employee.__name__:", Calcution.__name__)
    print ("Employee.__module__:", Calcution.__module__)
    print ("Employee.__bases__:", Calcution.__bases__)
    print ("Employee.__dict__:", Calcution.__dict__)

