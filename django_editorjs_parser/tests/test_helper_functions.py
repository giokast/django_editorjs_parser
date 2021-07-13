import pytest

from ..src.helpers import sanitize_HTML, add_method_to

# contains no methods
class A: 
    pass


class TestHelperFunctions():

    def test_class_A_has_no_function_named_foo(self):
        a = A()

        def foo():
            print('foo')

        with pytest.raises(AttributeError) as ae:
            a.foo()
    
    def test_add_method_to_decorator_adds_function_to_class(self):
        a = A()

        @add_method_to(A)
        def foo():
            print('foo')

        a.foo()

