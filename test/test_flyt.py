import pytest
from src import flyt


def test_validate_argument_channel_name():
    arg = 'randomChannel'
    ytname = flyt.validateArgument(arg)
    assert ytname == 'https://www.youtube.com/user/' + arg + '/videos'


def test_validate_argument_whole_link():
    arg = 'http://www.youtube.com/user/randomChannel'
    ytname = flyt.validateArgument(arg)
    assert ytname == arg + '/videos'


def test_validate_argument_without_http():
    arg = 'www.youtube.com/user/randomChannel'
    ytname = flyt.validateArgument(arg)
    assert ytname == 'https://' + arg + '/videos'


def test_validate_argument_without_www():
    arg = 'youtube.com/user/randomChannel'
    ytname = flyt.validateArgument(arg)
    assert ytname == 'https://' + arg + '/videos'


def test_get_latest_video_list_404():
    arg = 'testtesttesttesttesttest'
    with pytest.raises(SystemExit) as se:
        flyt.getLatestVideosList(arg, 5)
    assert se.value.message == '404'


def test_prettify_bad_html():
    testHtml = "<html><div class='yt-lockup-content'></div></html>"
    with pytest.raises(SystemExit) as se:
        flyt.prettify(testHtml, 5)
    assert se.value.message == 'Error: list index out of range'
