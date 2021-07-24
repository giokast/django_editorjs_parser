from functools import wraps



# source: https://mgarod.medium.com/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6
def add_method_to(cls):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        return func
    return decorator


def sanitize_HTML(markup):
    markup = markup.replace('/&/g', '&amp;')
    markup = markup.replace('/</g', '&lt;')
    markup = markup.replace('/>/g', '&gt;')
    return markup
