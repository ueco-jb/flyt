#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests
import sys


def validateArgument(argument):
        pattern = re.compile('^((https?)\:\/\/)?((www\.)?'
                             'youtube\.com|youtu\.?be)\/user\/.+$')
        if pattern.match(argument):
            return argument + '/videos'
        else:
            return "https://www.youtube.com/user/" + argument + '/videos'


def prettify(htmlResponse):
    soup = BeautifulSoup(htmlResponse, 'html.parser')
    for vidObject in soup.find_all('div', {'class': 'yt-lockup-content'})[:5]:
        video = vidObject.contents[1].a
        date = vidObject.contents[3].ul.contents[1].get_text()
        try:
            print("{0} - https://www.youtube.com{1} - {2}"
                  .format(video['title'].encode('utf-8'), video['href'], date))
        except Exception as e:
            print("Error: {}".format(e))


def getLatestVideosList():
    try:
        ytname = validateArgument(sys.argv[1])
    except:
        print("Lack of argument!")
        sys.exit(1)

    header = {'user-agent': 'Mozilla/3.0', 'Accept-Language': 'en-US,en;q=0.5'}
    r = requests.get(ytname, headers=header)
    if r.status_code == 200:
        prettify(r.text)
    else:
        print(r.status_code)


def main():
    getLatestVideosList()


if __name__ == "__main__":
    main()
