import pytest

from ..src.helpers import sanitize_HTML, add_method_to, deep_copy_dict

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

    def test_deep_copying_of_dicts(self):

        dict_1  = {
            'dog' : 'cat', 
            'horse' :'goat'
        }

        dict_2 = { 
            'usop' : 'shoot', 
            'horse' : 'bla'
        }

        deep_copied_dict = deep_copy_dict(dict_1, dict_2)

        correct_dict = {
            'dog' : 'cat', 
            'usop' : 'shoot',
            'horse' : 'bla'
        }

        assert deep_copied_dict == correct_dict
    
    def test_deep_copying_of_dicts_1_layer(self):

        dict_1  = {
            'dog' : 'cat', 
            'horse' :'bla'
        }

        dict_2 = { 
            'usop' : 'shoot', 
            'horse' : {
                'true' : 'false',
                'yes' : 'no'
            }
        }

        deep_copied_dict = deep_copy_dict(dict_1, dict_2)

        correct_dict = {
            'dog' : 'cat', 
            'usop' : 'shoot',
            'horse' : {
                'true' : 'false',
                'yes' : 'no'
            }
        }

        assert deep_copied_dict == correct_dict
    
    def test_deep_copying_of_nested_dicts_2_layers(self):

        dict_1  = {
            'dog' : 'cat', 
            'horse' : {
                'black' : 'beauty',
                'white': { 
                    'cool' : 'wow'
                }
            }
        }

        dict_2 = { 
            'usop' : 'shoot', 
            'horse' : {
                'black' : 'weather', 
                'robin': 'hands', 
            }
        }

        deep_copied_dict = deep_copy_dict(dict_1, dict_2)

        correct_dict = {
            'dog' : 'cat', 
            'usop' : 'shoot',
            'horse' : {
                'black' : 'weather',
                'robin' : 'hands',
                'white': { 
                    'cool' : 'wow',
                }
            }
        }

        assert deep_copied_dict == correct_dict

