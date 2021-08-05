from setuptools import setup

setup(
    name = 'django_editorjs_parser',
    packages = ['django_editorjs_parser'],
    py_modules = ['django_editorjs_parser.src'],
    version = '0.1.4',
    license = 'MIT',
    description = 'Parser for clean-blocks used by editor-js written in python',
    author='giovkast',
    author_email='giovkast@gmail.com',
    url = 'https://github.com/giokast/python_editorjs_parser',
    download_url = 'https://github.com/giokast/django_editorjs_parser/archive/refs/tags/0.1.4.tar.gz',

    keywords = '',
    install_requires = [

    ],
    classifiers = [ 
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False)