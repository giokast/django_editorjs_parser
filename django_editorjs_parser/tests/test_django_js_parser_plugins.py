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

    def test_code_plugin_correct_html(self):

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
        