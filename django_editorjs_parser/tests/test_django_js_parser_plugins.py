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

    def test_ordered_list_plugin_returns_correct_html(self):

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


    # difference ordered vs unordered list: https://sabe.io/classes/html/lists
    # test not necessary
    def test_unordered_list_plugin_returns_correct_html(self):

        data =  {
                "type": "list",
                "data": {
                    "style": "unordered",
                    "items": [
                        "Search Engine",
                        "Google fonts",
                        "Google images",
                        "Google maps"
                    ]
                }
        }
        pass

    def test_paragraph_plugin_returns_correct_html(self):
        
        assert False

        
        