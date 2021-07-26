from functools import wraps



# source: https://mgarod.medium.com/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6
def add_method_to(cls):
    "A decorator to dynamically add a function to a class when defining a new function"
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        return func
    return decorator


def sanitize_HTML(markup):
    "replace markup to sanitize HTML"
    markup = markup.replace('/&/g', '&amp;')
    markup = markup.replace('/</g', '&lt;')
    markup = markup.replace('/>/g', '&gt;')
    return markup


def nested_dict_copy(dict_1, dict_2):
    "copies or appends the keys of nested dicts"
    for k,v in dict_2.items():
        if k in dict_1:
            if isinstance(dict_1.get(k), str):
                dict_1[k] = dict_2[k]
            elif isinstance(dict_1.get(k), dict):
                nested_dict_copy(dict_1[k], dict_2[k])
        else: 
            dict_1[k] = v



    return dict_1