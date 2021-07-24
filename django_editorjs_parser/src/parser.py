from .config import ParserConfig
from .plugins import DefaultPlugins

from .helpers import deep_copy_dict

class EditorJSParser:

    def __init__(self, config = {}, custom_plugins = {}, custom_embeds = {}):
        self.config = ParserConfig()._conf

        self.plugins = DefaultPlugins()

        self.embeds = ParserConfig().get_property('embed')
        if custom_embeds:
            self.embeds = deep_copy_dict(self.embeds, custom_embeds)

    def parse(self, editorjs_object):
        markup = map(self.parse_block, editorjs_object['blocks'])
        html = ' '.join(list(markup))
        return html
    
    def parse_block(self, block):
        plugin_name = block['type']

        methods_list = dir(DefaultPlugins)
        
        if plugin_name in methods_list:
            method = getattr(DefaultPlugins, plugin_name)
            markup = method(block, config=ParserConfig().get_property(plugin_name))
            return markup
        
        return "<div> empty </div>"
    



