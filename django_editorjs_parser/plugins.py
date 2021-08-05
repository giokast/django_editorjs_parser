from . import config
from .helpers import sanitize_HTML

import re

from functools import reduce

class DefaultPlugins:


    @staticmethod
    def header(block, *args, **kwargs):
        data = block['data']
        return f"<h{data['level']}>{data['text']}</h{data['level']}>"

    @staticmethod
    def list(block, *args, **kwargs):
        data = block['data']
        type_of_list = "ol" if data['style'] == "ordered" else "ul"

        html_list = [f"<li> {item} </li>" for item in data['items']]

        return f"<{type_of_list}> {' '.join(map(str,html_list))} </{type_of_list}>"

    @staticmethod
    def paragraph(block, *args, **kwargs):
        data = block['data']
        config = kwargs['config']
        return f"<p class='{config['pClass']}'> {data['text']} </p>"

    @staticmethod
    def code(block, *args, **kwargs):
        data = block['data']
        config = kwargs['config']
        markup = sanitize_HTML(data['code'])
        return f"<pre><code> class='{config['codeBlockClass']}'> {data['code']} </code><pre>"
    
    @staticmethod
    def delimiter(block, *args, **kwargs):
        return "</br>"
    
    @staticmethod
    def raw(block, *args, **kwargs):
        data = block['data']
        return data['html']

    

    @staticmethod
    def embed(block, *args, **kwargs):

        data = block['data']
        config = kwargs['config']
        data['length'] = ""
        if config['useProvidedLength']: 
            data['length'] = f"width='{data['width']}' height='{data['height']}'"
        

        def replace_with_dict_key(m):
            return data[m.group(1)]

        # backreferencing with regex matching: 
        # using functions for replacement logic in re.sub: 
        regex = re.compile('<{data\.(.+?)}>')

        try:
            service_markup = config['embedMarkups'][data['service']]
        except KeyError as e:
            print(e)
            service_markup = config['embedMarkups']['default_markup']
        finally: 
            formatted_service_markup = re.sub(regex, replace_with_dict_key, service_markup)
            return formatted_service_markup
        
    @staticmethod
    def table(block, *args, **kwargs):
        data = block['data']['content']

        table_data = ""
        for entry in data: 
            table_row = ""
            for data in entry:
                table_row += "<td>'" + data + "'</td>"
            table_data += "<tr>" + table_row + "</tr>"

        return "<table><tbody>" + table_data + "</tbody></table>"
    
    @staticmethod
    def image(block, *args, **kwargs):
        data = block['data']
        config = kwargs['config']
        img_is_full_width =  "img-fullwidth" if (data['stretched']) else "" 
        img_has_border = "img_border" if (data['withBorder']) else ""
        img_has_background = "img-bg" if (data['withBackground']) else ""
        img_conditions = " " + img_is_full_width + " " + img_has_border + " " + img_has_background

        img_class = ""
        try: 
            img_class = config['imgClass']
        except KeyError as e:
            print('Key doenst exist')
        
        img_source = ""

        if data['url']:
            img_source = data['url']
        elif config['path'] == 'absolute':
            img_source = data['file']['url']
        else: 
            #ToDo
            pass

        if config['use'] == 'img':
            return f"<img class='{img_conditions} {img_class}' src='{img_source}' alt='{data['caption']}"
        elif config['use'] == 'figure':

            figure_class = config['figureClass'] or ""
            figure_caption_class = config['figCapClass'] or ""
            
            return f'<figure class="${figure_class}"><img class="${img_class} ${img_conditions}" src="${img_source}" alt="${data["caption"]}"><figcaption class="${figure_caption_class}">${data["caption"]}</figcaption></figure>'

        return ""


