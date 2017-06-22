from distutils.core import setup
setup(
    name = 'flyt',
    packages = ['flyt'],
    version = '0.1',
    description = 'Fetch Latest YouTube videos from given channel',
    author = 'Jakub Bogucki',
    author_email = 'jbogucki@libertymail.net',
    license = 'MIT',
    url = 'https://github.com/jakubbogucki/flyt',
    download_url = 'https://github.com/jakubbogucki/flyt/archive/0.1.tar.gz',
    keywords = ['flyt', 'fetch', 'latest', 'youtube', 'video', 'channel'],
    classifiers = [],
    scripts=['flyt/flyt'],
)
