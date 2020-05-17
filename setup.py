import setuptools
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name="pysnip",
    version="1.2.0",
    description="Python snippets",
    long_description=read("README.md"),
    url="https://github.com/AgeOfMarcus/pysnip",
    author="AgeOfMarcus",
    author_email="marcus@marcusweinberger.com",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=['requests'],
)