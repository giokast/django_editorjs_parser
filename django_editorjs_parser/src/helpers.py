

def sanitize_HTML(markup):
    markup = markup.replace('/&/g', '&amp;')
    markup = markup.replace('/</g', '&lt;')
    markup = markup.replace('/>/g', '&gt;')
    return markup


def get_embedded_markups():

    markup_dict = { 
        'youtube': '<div class="embed"><iframe class="embed-youtube" frameborder="0" src="<{data.embed}>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen <{data.length}>></iframe></div>',

        'twitter': '<blockquote class="twitter-tweet" class="embed-twitter" <{data.length}>><a href="<{data.source}>"></a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>',

        'instagram': '<blockquote class="instagram-media" <{data.length}>><a href="<{data.embed}>/captioned"></a></blockquote><script async defer src="//www.instagram.com/embed.js"></script>',

        'codepen': '<div class="embed"><iframe <{data.length}> scrolling="no" src="<{data.embed}>" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true"></iframe></div>',

        'defaultMarkup': '<div class="embed"><iframe src="<{data.embed}>" <{data.length}> class="embed-unknown" allowfullscreen="true" frameborder="0" ></iframe></div>',
    }

    return markup_dict