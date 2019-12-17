from StundetD import Student, StudentOp


import os.path

def test_add():
    s = Student(1, "A")
    so = StudentOp()
    assert so.add(s) == True


def test_fetch_all():
    so = StudentOp()
    assert type(so.fetch_all()) == type([])

def test_getssh(monkeypatch):
    monkeypatch.setattr("StudentD.StudentFile",Mock())

