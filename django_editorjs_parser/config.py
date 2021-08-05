
# https://www.hackerearth.com/practice/notes/samarthbhargav/a-design-pattern-for-configuration-management-in-python/



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
        #  set to true if you want the returned width and height of editorjs to be applied
        #  NOTE: sometimes source site overrides the lengths so it does not work 100%
        'useProvidedLength': False,
        'embedMarkups' : { 
            
            'youtube': '<div class="embed"><iframe class="embed-youtube" frameborder="0" src="<{data.embed}>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen<{data.length}>></iframe></div>',

            'twitter': '<blockquote class="twitter-tweet" class="embed-twitter"<{data.length}>><a href="<{data.source}>"></a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>',

            'instagram': '<blockquote class="instagram-media"<{data.length}>><a href="<{data.embed}>/captioned"></a></blockquote><script async defer src="//www.instagram.com/embed.js"></script>',

            'codepen': '<div class="embed"><iframe <{data.length}>scrolling="no" src="<{data.embed}>" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true"></iframe></div>',

            'default_markup': '<div class="embed"><iframe src="<{data.embed}>"<{data.length}> class="embed-unknown" allowfullscreen="true" frameborder="0" ></iframe></div>',
        }
    },
    'quote': {
        'applyAlignment': False,
        # if set to true blockquote element will have text-align css property set
    },

}

class BaseConfig(object):

    def __init__(self):

        self._conf = conf

    def get_property(self, property_name):
        if property_name not in self._conf.keys():
            return ValueError("property doesn't exist")
        else:
            return self._conf[property_name]
    
    def set_property(self, property_name, value):
        if property_name not in self._conf.keys():
            return ValueError("property doesn't exist")
        else: 
            self._conf[property_name] = value


class ParserConfig(BaseConfig):

    @property
    def image_conf(self):
        return self.get_property('image')

    @property
    def paragraph_conf(self):
        return self.get_property('paragraph')

    @property
    def code_conf(self):
        return self.get_property('code')

    @property
    def embed_conf(self):
        return self.get_property('embed')

    @property
    def quote_conf(self):
        return self.get_property('quote')

