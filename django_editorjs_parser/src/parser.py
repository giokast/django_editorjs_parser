from .config import ParserConfig

class EditorJSParser:

    def __init__(self, config = {}, custom_parsers = {}, custom_embeds = {}):
        self.config = ParserConfig()
        # append custom functions to 
        self.parsers = 'bla'
        self.config.embed.append = 'bla'

    def parse(self):
        pass
    
    def parse_block(self, block):
        pass