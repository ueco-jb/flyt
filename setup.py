#!/usr/bin/env python2

from setuptools import setup

setup(
    name = 'flyt',
    packages = ['src'],
    version = '0.3',
    description = 'Fetch Latest YouTube videos from given channel',
    author = 'Jakub Bogucki',
    author_email = 'jbogucki@libertymail.net',
    license = 'MIT',
    url = 'https://github.com/jakubbogucki/flyt',
    download_url = 'https://github.com/jakubbogucki/flyt/archive/0.3.tar.gz',
    keywords = ['flyt', 'fetch', 'latest', 'youtube', 'video', 'channel'],
    classifiers = [],
    scripts = ['src/flyt.py'],
    entry_points = {
        'console_scripts': [
            'flyt = flyt:main'
        ]
    },
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
)
