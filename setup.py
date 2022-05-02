###Copyright owned by HOStudio[@hopy]$ author (QQ Name)
###Copyright owned by HOStudio123 author (Github Name)
###Copyright owned by HOStudio6666 author (Pypi Name)
###Copyright owned by HOStudio6666 author (TestPypi Name)
import setuptools
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name = 'HOPYBOX',
    version = '1.3.28',
    author = 'ChenJinLin',
    author_email = 'hostudio.hopybox@foxmail.com',
    description = '''
This is an open source, practical and exquisite command box
''',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/HOStudio123/HOPYBOX',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.8',
    install_requires = ['wget','bs4','requests','lxml>=4.6.0','filetype','yagmail','rich']
)