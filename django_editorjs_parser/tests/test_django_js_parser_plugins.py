from ..src.plugins import Plugins

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
        
        assert False


    def test_paragraph_plugin_returns_correct_html(self):
        
        assert False

        
        