import datetime

from youtube import PLVideo


def test_get_attributes_when_video_in_playlist(video_in_playlist_from_json):

    assert video_in_playlist_from_json.title == 'Пушкин: наше все?'
    assert video_in_playlist_from_json.url == 'https://www.youtube.com/watch?v=BBotskuyw_M'
    assert video_in_playlist_from_json.view_count == 507414
    assert video_in_playlist_from_json.like_count == 18523
    assert video_in_playlist_from_json.id_playlist == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
    assert video_in_playlist_from_json.duration == datetime.timedelta(seconds=6738)


def test_get_attributes_when_video_not_in_playlist(video_not_playlist_from_json):

    assert video_not_playlist_from_json.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video_not_playlist_from_json.url == 'https://www.youtube.com/watch?v=9lO06Zxhu88'
    assert video_not_playlist_from_json.view_count == 49345436
    assert video_not_playlist_from_json.like_count == 976215
    assert video_not_playlist_from_json.id_playlist == 'Видео "Как устроена IT-столица мира' \
                                                       ' / Russian Silicon Valley (English subs)" ' \
                                                       'нет в указанном плейлисте'
    assert video_not_playlist_from_json.duration == datetime.timedelta(seconds=11253)


def test_get_video_in_playlist_by_id():
    video = PLVideo(playlist_id='PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD', video_id='BBotskuyw_M')
    assert str(video) == 'Пушкин: наше все?'
