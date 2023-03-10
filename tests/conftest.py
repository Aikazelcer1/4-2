import os

import pytest

from youtube import Channel, Video, PLVideo, PlayList

PATH_TO_TEST_CHANNEL_1_JSON = os.path.join('tests', 'data/test_channel_1.json')
PATH_TO_TEST_CHANNEL_2_JSON = os.path.join('tests', 'data/test_channel_2.json')
PATH_TO_TEST_VIDEO_JSON = os.path.join('tests', 'data/test_video.json')
PATH_TO_TEST_VIDEO_IN_PLAYLIST_JSON = os.path.join('tests', 'data/test_video_in_playlist.json')
PATH_TO_VIDEO_IN_PLAYLIST_JSON = os.path.join('tests', 'data/video_in_playlist.json')
PATH_TO_VIDEO_NOT_PLAYLIST_JSON = os.path.join('tests', 'data/video_not_playlist.json')
PATH_TO_PLAYLIST_JSON = os.path.join('tests', 'data/test_playlist.json')


@pytest.fixture
def channel_1_from_json():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_1_JSON)


@pytest.fixture
def channel_2_from_json():
    return Channel(channel_json=PATH_TO_TEST_CHANNEL_2_JSON)


@pytest.fixture
def channel_from_youtube():
    return Channel(channel_id='UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def video_from_json():
    return Video(video_json=PATH_TO_TEST_VIDEO_JSON)


@pytest.fixture
def video_from_youtube():
    return Video(video_id='9lO06Zxhu88')


@pytest.fixture
def video_in_playlist_from_json():
    return PLVideo(video_json=PATH_TO_TEST_VIDEO_IN_PLAYLIST_JSON, playlist_json=PATH_TO_VIDEO_IN_PLAYLIST_JSON)


@pytest.fixture
def video_not_playlist_from_json():
    return PLVideo(video_json=PATH_TO_TEST_VIDEO_JSON, playlist_json=PATH_TO_VIDEO_NOT_PLAYLIST_JSON)


@pytest.fixture
def playlist_from_json():
    return PlayList(playlist_json=PATH_TO_PLAYLIST_JSON)


@pytest.fixture
def playlist_from_youtube():
    return PlayList(playlist_id='PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')