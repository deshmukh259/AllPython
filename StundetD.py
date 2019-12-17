import json
from student_db import StudentFile


class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return str({"id": self.id, "name": self.name})


class StudentOp:
    def __init__(self, sf):
        self.sf = sf

    def add(self, s):
        return self.sf.add_to_file(s)

    def fetch_all(self):
        return self.sf.fetch_all()


if __name__ == "__main__":
    c = StudentFile()
    c.fetch_all()
