from setuptools import setup


from svggearslib import __version__, __author__

setup(
    name='svggears',
    version=__version__,
    author=__author__,
    py_modules=['svggears'],
    packages=['svggearslib'],
    install_requires=[
     'numpy',
     'colorama',
    ],
    entry_points='''
        [console_scripts]
        svggears=svggears:cli
    ''',
)
