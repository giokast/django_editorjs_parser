import pytest

from ..src.parser import EditorJSParser

class Test_EditorJSParser: 

    ###########3 Test Constructor ###################

    def test_constuctors_with_empty_parameters(self):
        parser = EditorJSParser()



    def test_constructor_with_custom_config(self):
        pass

    def test_constructor_with_custom_embeds(self):
        assert False  

    def test_constructor_with_custom_parsers(self):
        # check if after constructing with custom parser
        # the custom function should be in the list of functions belonging to the class
        pass
    

    ###########3 Test Parser ###################3