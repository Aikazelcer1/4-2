import os.path

import pytest

from youtube import Channel


def test_get_attributes(channel_1_from_json):

    assert channel_1_from_json.title == 'вДудь'
    assert channel_1_from_json.description == 'Здесь задают вопросы'
    assert channel_1_from_json.link == '@vdud'
    assert channel_1_from_json.subscriber_count == 10300000
    assert channel_1_from_json.video_count == 164
    assert channel_1_from_json.view_count == 1946788891


def test_channel_info_attribute_access(channel_1_from_json):

    with pytest.raises(AttributeError):
        channel_info = channel_1_from_json.channel_info


def test_exception():

    with pytest.raises(Exception):
        channel = Channel()


def test_object_name_str(channel_from_youtube):

    assert str(channel_from_youtube) == 'YouTube-канал: вДудь'


def test_object_name_repr(channel_from_youtube):

    assert repr(channel_from_youtube) == 'Channel(channel_id=UCMCgOm8GZkHp8zJ6l7_hIuA)'


def test_to_json(channel_1_from_json):

    channel_1_from_json.to_json()
    file_path = 'None.json'
    os.path.exists(file_path)
    os.remove(file_path)


def test_len(channel_1_from_json):

    assert len(channel_1_from_json) == 10300000


def test_add(channel_1_from_json, channel_2_from_json):

    assert channel_1_from_json + channel_2_from_json == 13980000


def test_add_exception(channel_1_from_json):

    with pytest.raises(ArithmeticError):
        result = channel_1_from_json + 10


def test_gt(channel_1_from_json, channel_2_from_json):

    assert channel_1_from_json > channel_2_from_json
    assert channel_2_from_json < channel_1_from_json


def test_gt_exception(channel_1_from_json):

    with pytest.raises(TypeError):
        result = channel_1_from_json > 10


def test_incorrect_id_channel(channel_1_from_json):

    channel = Channel(channel_id='test')
    assert channel.channel_id == 'test'
    assert channel.title is None
    assert channel.description is None
    assert channel.link is None
    assert channel.subscriber_count is None
    assert channel.video_count is None
    assert channel.view_count is None
    assert len(channel) == 0
    assert channel + channel_1_from_json is None
    assert (channel < channel_1_from_json) is None
