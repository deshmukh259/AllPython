import json


class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return str({"id": self.id, "name": self.name})


class StudentOp:
    def add(self, s):
        sf = StudentFile()
        return sf.add_to_file(s)

    def fetch_all(self):
        sf = StudentFile()
        return sf.fetch_all()


class StudentFile:

    def add_to_file(self, st):
        try:
            with open("C:/clone/PyD.txt", "a") as f:
                f.write(str(st) + "\n")
        except:
            return False
        return True

    def fetch_all(self):
        try:
            ll = []
            print("LL")
            with open("C:/clone/PyD.txt") as f:
                for l in f:
                    print(l)
                    l = l.replace("'", "\"")
                    d = json.loads(l)
                    s = Student(d['id'], d['name'])
                    print (s)
                    ll.append(s)

            print ("List", len(ll))
            return ll
        except Exception as e:
            print(e)

        return None


if __name__ == "__main__":
    c = StudentFile()
    c.fetch_all()
