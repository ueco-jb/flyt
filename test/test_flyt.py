import pytest
import sys, os
sys.path.append(os.path.abspath('..'))
from src import flyt

def test_validate_argument_channel_name():
    arg = "randomChannel"
    ytname = flyt.validateArgument(arg)
    assert ytname == 'https://www.youtube.com/user/' + arg + '/videos'

def test_validate_argument_whole_link():
    arg = 'http://www.youtube.com/user/randomChannel'
    ytname = flyt.validateArgument(arg)
    assert ytname == 'http://www.youtube.com/user/randomChannel/videos'
