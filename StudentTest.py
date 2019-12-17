from StundetD import Student, StudentOp
from student_db import StudentFile
import mock
import pytest


@pytest.fixture
def mock_st_db():
    return mock.Mock(StudentFile)


def test_add(mock_st_db):
    print(dir(mock_st_db))
    mock_st_db.add_to_file.return_value=True
    s = Student(1, "A")
    so = StudentOp(mock_st_db)
    assert so.add(s) == True


def test_fetch_all():
    so = StudentOp()
    assert type(so.fetch_all()) == type([])
