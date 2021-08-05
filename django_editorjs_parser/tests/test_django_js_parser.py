import pytest

from ..parser import EditorJSParser

class Test_EditorJSParser: 

    ###########3 Test Constructor ###################

    def test_constuctors_with_empty_parameters(self):
        parser = EditorJSParser()
        pass


    def test_constructor_with_custom_config(self):
        pass

    def test_constructor_with_custom_embeds(self):
        pass

    def test_constructor_with_custom_parsers(self):
        # check if after constructing with custom parser
        # the custom function should be in the list of functions belonging to the class
        pass
    

    ###########3 Test Parser ###################3

    def test_parsing_of_block(self):
        parser = EditorJSParser()

        data = {
                "time": 1601898039654,
                "blocks": [{
                        "type": "image",
                        "data": {
                            "url": "https://www.tesla.com/tesla_theme/assets/img/_vehicle_redesign/roadster_and_semi/roadster/hero.jpg",
                            "caption": "Roadster // tesla.com",
                            "withBorder": False,
                            "withBackground": False,
                            "stretched": True
                        }
                    },
                    {
                        "type": "paragraph",
                        "data": {
                            "text": "Hello There, it is a test post related to <a href=\"https://google.com\">Google</a> which is the <b>biggest</b> search engine!"
                        }
                    },
                    {
                        "type": "header",
                        "data": {
                            "text": "Google's attributes",
                            "level": 2
                        }
                    },
                    {
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
                    },
                    {
                        "type": "quote",
                        "data": {
                            "text": "If your access to health care involves your leaving work and driving somewhere and parking and waiting for a long time, that's not going to promote healthiness.",
                            "caption": "Larry Page",
                            "alignment": "left"
                        }
                    },
                ]}
        
        
        html = parser.parse(data)

        assert html ==  '<figure class="$fig-img"><img class="$img $ img-fullwidth  " src="$https://www.tesla.com/tesla_theme/assets/img/_vehicle_redesign/roadster_and_semi/roadster/hero.jpg" alt="$Roadster // tesla.com"><figcaption class="$fig-cap">$Roadster // tesla.com</figcaption></figure> <p class=\'paragraph\'> Hello There, it is a test post related to <a href=\"https://google.com\">Google</a> which is the <b>biggest</b> search engine! </p> <h2>Google\'s attributes</h2> <ol> <li> Search Engine </li> <li> Google fonts </li> <li> Google images </li> <li> Google maps </li> </ol> <div> empty </div>'
        