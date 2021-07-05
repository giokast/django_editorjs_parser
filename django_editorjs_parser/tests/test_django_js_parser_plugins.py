from ..src.plugins import Plugins
from ..src.config import ParserConfig

class Test_Plugins:

    def test_header_plugin_returns_correct_html(self):

        data =  {
                "type": "header",
                "data": {
                    "text": "Google's attributes",
                    "level": 2
                }
            }

        correct_html = "<h2>Google's attributes</h2>"
        parsed_html = Plugins.header(data)

        assert correct_html == parsed_html

    def test_list_plugin_returns_correct_html(self):

        data =  {
                "type": "list",
                "data": {
                    "style": "ordered",
                    "items": [
                        "Search Engine",
                        "Google fonts",
                        "Google images",
                        "Google maps"
                    ]
                }
            }

        correct_html = "<ol> <li> Search Engine </li> <li> Google fonts </li> <li> Google images </li> <li> Google maps </li> </ol>"

        parsed_html = Plugins.list(data)

        assert correct_html == parsed_html
    
    def test_table_plugin_returns_correct_html(self):
        data = {
                "content": [
                    ["", "Me", "Me"],
                    ["You", "Ugly", "Big"]
                ]
            }

        correct_html = ""


        assert False


    def test_paragraph_plugin_returns_correct_html(self):

        para_config = ParserConfig().get_property('paragraph')
        data = {
                "type": "paragraph",
                "data": {
                    "text": "Hello There, it is a test post related to <a href=\"https://google.com\">Google</a> which is the <b>biggest</b> search engine!"
                }
            }
        
        correct_html = "<p class='paragraph'> Hello There, it is a test post related to <a href=\"https://google.com\">Google</a> which is the <b>biggest</b> search engine! </p>"

        parsed_html = Plugins.paragraph(data, para_config)

        assert correct_html == parsed_html

    def test_code_plugin_returns_correct_html(self):

        code_config = ParserConfig().get_property('code')
        data = {
            "type": "code",
            "data": {
                "code": "const path = require(\"path\");\nconst cookieParser = require(\"cookie-parser\");\n"
            }
        }        

        correct_html = "<pre><code> class='code-block'> const path = require(\"path\");\nconst cookieParser = require(\"cookie-parser\");\n </code><pre>"
        parsed_html = Plugins.code(data, code_config)

        assert correct_html == parsed_html
    
    def test_delimiter_plugin_returns_correct_html(self):
        
        data =  {
            "type": "delimiter"
        }

        correct_html = "</br>"
        parsed_html = Plugins.delimiter(data)

        assert correct_html == parsed_html
    
    def test_raw_plugin_returns_correct_html(self):
        
        data = {
            "type": "raw",
            "data": {
                "html": "<blockquote class=\"imgur-embed-pub\" lang=\"en\" data-id=\"a/Vd1xADQ\"  \
                            ><a href=\"//imgur.com/a/Vd1xADQ\">Dark arts and crafts!</a>"
            }
        }

        correct_html = "<blockquote class=\"imgur-embed-pub\" lang=\"en\" data-id=\"a/Vd1xADQ\"  \
                            ><a href=\"//imgur.com/a/Vd1xADQ\">Dark arts and crafts!</a>"
        
        parsed_html = Plugins.raw(data)


        assert correct_html == parsed_html
    
    def test_embed_plugin_returns_correct_html_for_instagram(self):

        embed_config = ParserConfig().get_property('embed')
        data =  {
            "type": "embed",
            "data": {
                "service": "instagram",
                "source": "https://www.instagram.com/p/CFuMV9MhwlL",
                "embed": "https://www.instagram.com/p/CFuMV9MhwlL/embed",
                "width": 400,
                "height": 505,
                "caption": ""
            }
        }

        correct_html = '<blockquote class="instagram-media"><a href="https://www.instagram.com/p/CFuMV9MhwlL/embed/captioned"></a></blockquote><script async defer src="//www.instagram.com/embed.js"></script>'
        parsed_html = Plugins.embed(data, embed_config)

        assert correct_html == parsed_html
    
    def test_embed_plugin_returns_correct_html_for_twitter(self):
        embed_config = ParserConfig().get_property('embed')
        data =  {
            "type": "embed",
            "data": {
                "service": "twitter",
                "source": "https://twitter.com/SpaceX/status/1310962850601545728",
                "embed": "https://twitframe.com/show?url=https://twitter.com/SpaceX/status/1310962850601545728",
                "width": 600,
                "height": 300,
                "caption": ""
            }
        }

        correct_html = '<blockquote class="twitter-tweet" class="embed-twitter"><a href="https://twitter.com/SpaceX/status/1310962850601545728"></a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'
        parsed_html = Plugins.embed(data, embed_config)

        assert correct_html == parsed_html

    def test_embed_plugin_returns_correct_html_for_codepen(self):
        embed_config = ParserConfig().get_property('embed')
        data =  {
            "type": "embed",
            "data": {
                "service": "codepen",
                "source": "https://codepen.io/traversbray/pen/NWNZwPq",
                "embed": "https://codepen.io/traversbray/embed/NWNZwPq?height=300&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2",
                "width": 600,
                "height": 300,
                "caption": ""
            }
        }

        correct_html = '<div class="embed"><iframe scrolling="no" src="https://codepen.io/traversbray/embed/NWNZwPq?height=300&amp;theme-id=0&amp;default-tab=css,result&amp;embed-version=2" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true"></iframe></div>'
        parsed_html = Plugins.embed(data, embed_config)
        assert correct_html == parsed_html

    def test_embed_plugin_returns_correct_html_for_youtube(self):
        embed_config = ParserConfig().get_property('embed')
        data =  {
            "type": "embed",
            "data": {
                "service": "youtube",
                "source": "https://www.youtube.com/watch?v=1z6sLQJHbP0",
                "embed": "https://www.youtube.com/embed/1z6sLQJHbP0",
                "width": 580,
                "height": 320,
                "caption": "This is a Youtube video!<br>"
            }
        }

        correct_html = '<div class="embed"><iframe class="embed-youtube" frameborder="0" src="https://www.youtube.com/embed/1z6sLQJHbP0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
        parsed_html = Plugins.embed(data, embed_config)
        assert correct_html == parsed_html

    def test_embed_plugin_defaults_to_defaultmarkup_for_unknown_service(self):
        embed_config = ParserConfig().get_property('embed')
        data =  {
            "type": "embed",
            "data": {
                "service": "waefa",
                "source": "https://www.youtube.com/watch?v=1z6sLQJHbP0",
                "embed": "https://www.youtube.com/embed/1z6sLQJHbP0",
                "width": 580,
                "height": 320,
                "caption": "This is a Youtube video!<br>"
            }
        }

        correct_html = '<div class="embed"><iframe src="https://www.youtube.com/embed/1z6sLQJHbP0" class="embed-unknown" allowfullscreen="true" frameborder="0" ></iframe></div>'
        parsed_html = Plugins.embed(data, embed_config)
        assert correct_html == parsed_html
