#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import argparse
import re
import requests
import sys


def validateArgument(argument):
    httpPattern = re.compile('^https?\:\/\/.*')
    pattern = re.compile('^.*((www\.)?youtube\.com)\/user\/.+$')
    if pattern.match(argument):
        if httpPattern.match(argument):
            return argument + '/videos'
        else:
            return 'https://' + argument + '/videos'
    else:
        return 'https://www.youtube.com/user/' + argument + '/videos'


def prettify(htmlResponse, length):
    soup = BeautifulSoup(htmlResponse, 'html.parser')
    for vidObject in soup.find_all('div',
                                   {'class': 'yt-lockup-content'})[:length]:
        try:
            video = vidObject.contents[1].a
            date = vidObject.contents[3].ul.contents[1].get_text()
            print("{0} - https://www.youtube.com{1} - {2}"
                  .format(video['title'].encode('utf-8'), video['href'], date))
        except Exception as e:
            sys.exit('Error: {}'.format(e))


def getLatestVideosList(argument, length):
    ytname = validateArgument(argument)
    header = {'user-agent': 'Mozilla/3.0', 'Accept-Language': 'en-US,en;q=0.5'}
    r = requests.get(ytname, headers=header)
    if r.status_code == 200:
        prettify(r.text, length)
    else:
        sys.exit(str(r.status_code))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('channel',
                        help='name of YT channel or http link to it')
    parser.add_argument('-l', '--length',
                        help='number of fetched records', type=int, default=5)
    args = parser.parse_args()

    getLatestVideosList(args.channel, args.length)


if __name__ == "__main__":
    main()
