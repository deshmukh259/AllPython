
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
