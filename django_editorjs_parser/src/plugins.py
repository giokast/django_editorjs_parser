

import re
from django_editorjs_parser.src.helpers import sanitize_HTML

class Plugins:


    @staticmethod
    def header(block):
        data = block['data']
        return f"<h{data['level']}>{data['text']}</h{data['level']}>"

    @staticmethod
    def list(block):
        data = block['data']
        type_of_list = "ol" if data['style'] == "ordered" else "ul"

        html_list = [f"<li> {item} </li>" for item in data['items']]

        return f"<{type_of_list}> {' '.join(map(str,html_list))} </{type_of_list}>"

    @staticmethod
    def paragraph(block, config):
        data = block['data']
        return f"<p class='{config['pClass']}'> {data['text']} </p>"

    @staticmethod
    def code(block, config):
        data = block['data']

        markup = sanitize_HTML(data['code'])
        return f"<pre><code> class='{config['codeBlockClass']}'> {data['code']} </code><pre>"
    
    @staticmethod
    def delimiter(block):
        return "</br>"
    
    @staticmethod
    def raw(block):
        data = block['data']
        return data['html']

    

    @staticmethod
    def embed(block, config):

        data = block['data']

        data['length'] = ""
        if config['use_provided_length']: 
            data['length'] = f"width='{data['width']}' height='{data['height']}'"
        

        def replace_with_dict_key(m):
            return data[m.group(1)]

        # backreferencing with regex matching: 
        # using functions for replacement logic in re.sub: 
        regex = re.compile('<{data\.(.+?)}>')

        try:
            service_markup = config['embed_markups'][data['service']]
        except KeyError as e:
            print(e)
            service_markup = config['embed_markups']['default_markup']
        finally: 
            formatted_service_markup = re.sub(regex, replace_with_dict_key, service_markup)
            return formatted_service_markup


            
        
    @staticmethod
    def table(block):
        return 0


