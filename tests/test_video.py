import datetime

import pytest

from youtube import Video


def test_get_attributes(video_from_json):

    assert video_from_json.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video_from_json.url == 'https://www.youtube.com/watch?v=9lO06Zxhu88'
    assert video_from_json.view_count == 49345436
    assert video_from_json.like_count == 976215
    assert video_from_json.duration == datetime.timedelta(seconds=11253)


def test_channel_info_attribute_access(video_from_json):

    with pytest.raises(AttributeError):
        video_info = video_from_json.video_info


def test_exception():

    with pytest.raises(Exception):
        video = Video()


def test_object_name_str(video_from_youtube):

    assert str(video_from_youtube) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_object_name_repr(video_from_youtube):

    assert repr(video_from_youtube) == 'Video(video_id=9lO06Zxhu88)'


def test_incorrect_video_id():

    video = Video(video_id='test')
    assert video.video_id == 'test'
    assert video.title is None
    assert video.url is None
    assert video.view_count is None
    assert video.like_count is None
    assert video.duration is None