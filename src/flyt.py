#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import argparse
import re
import requests
import sys, os
import curses
import pyperclip


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

class Video:
    def __init__(self, video_element):
        self.video_element = video_element
        self.element_content = video_element.contents[1].a
        self.title = self.element_content['title'].encode('utf-8')
        self.url = 'https://www.youtube.com'+self.element_content['href']
        self.date = 'LIVE' if video_element.find("span", {"class": "yt-badge-live"}) else video_element.contents[3].ul.contents[1].get_text()
    def to_string(self):
        return "{0} - {1} - {2}".format(self.title, self.url, self.date)


def get_video_list(argument, length):
    video_list = list()
    ytname = validateArgument(argument)
    header = {'user-agent': 'Mozilla/3.0', 'Accept-Language': 'en-US,en;q=0.5'}
    r = requests.get(ytname, headers=header)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        for video_element in soup.find_all('div',
                                       {'class': 'yt-lockup-content'})[:length]:
            try:
                video_object = Video(video_element) 
                video_list.append(video_object)
            except Exception as e:
                sys.exit('Error: {}'.format(e))
        return video_list
    else:
        sys.exit(str(r.status_code))

def my_menu(stdscr, video_list):

    cursor_pos = 0

    for i in range(0, len(video_list)):
        stdscr.addstr(i, 0, video_list[i].to_string(), curses.A_REVERSE if i == cursor_pos else 0)
    stdscr.addstr(i+2, 0, "Use the arrow keys (or vi keys) to move through the list")
    stdscr.addstr(i+3, 0, "Press ENTER to copy the URL to clipboard")
    stdscr.addstr(i+4, 0, "Press ESC to quit")
    stdscr.refresh()

    pressed_key = 0
    while pressed_key != 27:
        pressed_key = stdscr.getch()

        if (pressed_key == 106) or (pressed_key == 258):
            stdscr.addstr(cursor_pos, 0, video_list[cursor_pos].to_string(), 0)
            cursor_pos+=1
            cursor_pos=cursor_pos % len(video_list) 
            stdscr.addstr(cursor_pos, 0, video_list[cursor_pos].to_string(), curses.A_REVERSE)
        elif (pressed_key == 107) or (pressed_key == 259):
            stdscr.addstr(cursor_pos, 0, video_list[cursor_pos].to_string(), 0)
            cursor_pos-=1
            if cursor_pos < 0:
                cursor_pos+=len(video_list) 
            stdscr.addstr(cursor_pos, 0, video_list[cursor_pos].to_string(), curses.A_REVERSE)
        elif pressed_key == 10:
            pyperclip.copy(video_list[cursor_pos].url)
        stdscr.refresh()
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('channel',
                        help='name of YT channel or http link to it')
    parser.add_argument('-l', '--length',
                        help='number of fetched records', type=int, default=5)
    args = parser.parse_args()

    video_list = get_video_list(args.channel, args.length)
    curses.wrapper(my_menu, video_list)

if __name__ == "__main__":
    main()
