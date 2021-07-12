import pytest

from ..src.helpers import sanitize_HTML, add_method_to


# contains no methods
class A: 
    pass

def bla():
    print('bla')

@add_method_to
def foo():
    print('foo')

def Test_HelperFunctions():

    def test_add_method_to_adds_function_to_class(self):
        a = A()

        with pytest.raises(AttributeError) as ae:
            a.bla()
    
    def test_add_method_to_decorator_adds_functions_to_class(self):
        a = A()

        a.foo()

        assert False