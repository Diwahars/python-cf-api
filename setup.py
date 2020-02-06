from setuptools import setup
from os import path

setup(
    name='cf_api',
    version='2.0.0a1',
    description='Python Interface for Cloud Foundry APIs',
    long_description=open('README.md').read().strip(),
    long_description_content_type="text/markdown",
    license='Apache License Version 2.0',
    author='Adam Jaso',
    author_email='ajaso@hsdp.io',
    py_modules=['cf_api'],
    install_requires=['requests'],
    tests_require=['nose', 'responses', 'coverage', 'pdoc'],
    url='https://github.com/hsdp/python-cf-api',
)
