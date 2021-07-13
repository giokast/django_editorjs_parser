from ast import parse
from .config import ParserConfig
from .plugins import DefaultPlugins

class EditorJSParser:

    def __init__(self, config = {}, custom_plugins = {}, custom_embeds = {}):
        self.config = ParserConfig()._conf
        # append custom functions to 
        self.plugins = DefaultPlugins()

        self.embeds = ParserConfig().get_property('embed')
        if custom_embeds:
            for k,v in custom_embeds.items():
                self.embeds[k] = v

    def parse(self, editorjs_object):
        html = map(self.parse_block, editorjs_object['blocks'])
        print(list(html))
    
    def parse_block(self, block):
        type = block['type']

        bla = dir(DefaultPlugins)
        
        if type in bla:
            method = getattr(DefaultPlugins, type)
            markup = method(block, ParserConfig().get_property(type))
            return method


