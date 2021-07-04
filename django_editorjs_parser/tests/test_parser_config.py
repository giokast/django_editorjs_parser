from ..src.config import ParserConfig


class TestParserConfig():

    def test_get_property_get_image_conf(self):

        parser_conf = ParserConfig()
        image_config = parser_conf.image
        correct_image_conf = {
                'use': "figure", # figure or img (figcaption will be used for caption of figure)
                'imgClass': "img",
                'figureClass': "fig-img",
                'figCapClass': "fig-cap",
                'path': "absolute",
        }
        
        assert image_config == correct_image_conf

    def test_get_property_get_paragraph_conf(self):

        parser_conf = ParserConfig()
        paragraph_config = parser_conf.paragraph
        correct_paragraph_config = {
            'pClass': "paragraph",
        }
        
        assert paragraph_config == correct_paragraph_config

    def test_get_property_get_code_conf(self):

        parser_conf = ParserConfig()
        code_config = parser_conf.code
        correct_code_config = {
            'codeBlockClass': "code-block",
        }
        
        assert code_config == correct_code_config

    def test_get_property_get_embed_conf(self):

        parser_conf = ParserConfig()
        embed_config = parser_conf.embed
        correct_embed_config = {
            'useProvidedLength': False,
        }   
        
        assert embed_config == correct_embed_config


    def test_get_property_get_quote_conf(self):

        parser_conf = ParserConfig()
        quote_config = parser_conf.quote
        correct_quote_config =  {
                'applyAlignment': False,
        }
        

        assert quote_config == correct_quote_config