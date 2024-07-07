from setuptools import setup, find_packages

setup(
    name = 'montecarlo',
    version = '0.1.0',
    author = 'Luke Schneider',
    author_email = 'vrd9sd@virginia.edu',
    packages = find_packages(),
    url = 'https://github.com/lukeschneider7/DS5100-FP1/tree/main/montercarlo',
    license = 'LICENSE.txt',
    description = 'An awesome package that does something',
    long_description = open('README.txt').read(),
    install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)