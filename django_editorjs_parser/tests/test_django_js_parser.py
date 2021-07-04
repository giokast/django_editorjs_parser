import pytest

from ..src.parser import EditorJSParser

class Test_EditorJSParser: 

    ###########3 Test Constructor ###################3

    def test_constructor_with_empty_list(self):
        pass

    def test_constructor_with_list(self):
        assert False  

    def test_constructor_with_incorrect_input(self):
        with pytest.raises(ValueError):
            bla = EditorJSParser("")
    

    ###########3 Test Parser ###################3