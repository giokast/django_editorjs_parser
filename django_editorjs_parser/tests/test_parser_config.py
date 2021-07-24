import pytest

from ..src.config import ParserConfig, BaseConfig



class TestParserConfig():

    def test_get_image_conf(self):

        parser_conf = ParserConfig()
        image_config = parser_conf.image_conf
        correct_image_conf = {
                'use': "figure", 
                'imgClass': "img",
                'figureClass': "fig-img",
                'figCapClass': "fig-cap",
                'path': "absolute",
        }
        
        assert image_config == correct_image_conf

    def test_get_paragraph_conf(self):

        parser_conf = ParserConfig()
        paragraph_config = parser_conf.paragraph_conf
        correct_paragraph_config = {
            'pClass': "paragraph",
        }
        
        assert paragraph_config == correct_paragraph_config

    def test_get_code_conf(self):

        parser_conf = ParserConfig()
        code_config = parser_conf.code_conf
        correct_code_config = {
            'codeBlockClass': "code-block",
        }
        
        assert code_config == correct_code_config

    def test_get_embed_conf(self):

        parser_conf = ParserConfig()
        embed_config = parser_conf.embed_conf
        correct_embed_config = {
        'useProvidedLength': False,
        'embedMarkups' : { 
            
            'youtube': '<div class="embed"><iframe class="embed-youtube" frameborder="0" src="<{data.embed}>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen<{data.length}>></iframe></div>',

            'twitter': '<blockquote class="twitter-tweet" class="embed-twitter"<{data.length}>><a href="<{data.source}>"></a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>',

            'instagram': '<blockquote class="instagram-media"<{data.length}>><a href="<{data.embed}>/captioned"></a></blockquote><script async defer src="//www.instagram.com/embed.js"></script>',

            'codepen': '<div class="embed"><iframe <{data.length}>scrolling="no" src="<{data.embed}>" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true"></iframe></div>',

            'default_markup': '<div class="embed"><iframe src="<{data.embed}>"<{data.length}> class="embed-unknown" allowfullscreen="true" frameborder="0" ></iframe></div>',
        }
    }
        
        assert embed_config == correct_embed_config


    def test_get_quote_conf(self):

        parser_conf = ParserConfig()
        quote_config = parser_conf.quote_conf
        correct_quote_config =  {
                'applyAlignment': False,
                
        }

        assert quote_config == correct_quote_config

class TestBaseConfig():

    def test_value_error_raised_when_getting_non_existing_configuration_property(self):

        conf = BaseConfig()
        
        returned_exception = conf.get_property('sdfasdf')

        assert type(returned_exception) == ValueError
    
    def test_can_set_conf_to_new_values(self):
        conf = BaseConfig()

        new_value = "new value"
        conf.set_property('embed', "new value")
        embed_conf = conf.get_property('embed')

        assert embed_conf == new_value