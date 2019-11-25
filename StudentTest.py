from StundetD import Student, StudentOp



def test_add():
    s = Student(1, "A")
    so = StudentOp()
    assert so.add(s) == True


def test_fetch_all():
    so = StudentOp()
    assert type(so.fetch_all()) == type([])

