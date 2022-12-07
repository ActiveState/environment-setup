import sys

def test_python():
    py_info = sys.version_info
    assert py_info.major == 3 and py_info.minor==10

