from distutils.core import setup

setup(
    name='designernews_api',
    packages=['dn',],
    version='0.2',
    description='Python API for Designer News.',
    install_requires=['BeautifulSoup4>=4.3.1', 'requests'],
    author='Jannik Weyrich',
    author_email='jannikweyrich@gmail.com',
    url='https://github.com/j7nn7k/designernews_api', # use the URL to the github repo
    download_url='https://github.com/j7nn7k/designernews_api/tarball/0.1', # I'll explain this in a second
    keywords=['designer news', 'designernews', 'designernews api', 'designer news api', 'designernews_api'],
    classifiers=[],
)