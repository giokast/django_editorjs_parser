conf = {
    'image': {
        'use': "figure", # figure or img (figcaption will be used for caption of figure)
        'imgClass': "img",
        'figureClass': "fig-img",
        'figCapClass': "fig-cap",
        'path': "absolute",
    },
    'paragraph': {
        'pClass': "paragraph",
    },
    'code': {
        'codeBlockClass': "code-block",
    },
    'embed': {
        'useProvidedLength': False,
        #  set to true if you want the returned width and height of editorjs to be applied
        #  NOTE: sometimes source site overrides the lengths so it does not work 100%
    },
    'quote': {
        'applyAlignment': False,
        # if set to true blockquote element will have text-align css property set
    },
}

class Config(object):

    def __init__(self):
        self._conf = conf


    def get_property(self, property_name):
        if property_name not in self._conf.keys():
            return None
        else:
            return self._conf[property_name]


class ParserConfig(Config):

    @property
    def image(self):
        return self.get_property('image')

    @property
    def paragraph(self):
        return self.get_property('paragraph')

    @property
    def code(self):
        return self.get_property('code')

    @property
    def embed(self):
        return self.get_property('embed')

    @property
    def quote(self):
        return self.get_property('quote')

