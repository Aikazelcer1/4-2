import datetime
import json
import os
from typing import List

import isodate
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Youtube:


    YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    @classmethod
    def get_channel(cls, channel_id: str) -> dict:

        channel = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    @classmethod
    def get_video(cls, video_id: str) -> dict:

        video = cls.youtube.videos().list(id=video_id, part='snippet,statistics,contentDetails').execute()
        return video

    @classmethod
    def get_video_in_playlist(cls, video_id: str, playlist_id: str) -> dict:

        video_in_playlist = cls.youtube.playlistItems().list(
            part="snippet", playlistId=playlist_id, videoId=video_id
        ).execute()
        return video_in_playlist

    @classmethod
    def get_playlist(cls, playlist_id: str) -> dict:

        playlist = cls.youtube.playlists().list(id=playlist_id, part='snippet,contentDetails', maxResults=50).execute()
        return playlist

    @classmethod
    def get_playlist_video_ids(cls, playlist_id: str) -> List[str]:

        video_ids = []
        params = {'playlistId': playlist_id, 'part': 'snippet,contentDetails', 'maxResults': 50}
        while True:
            try:
                playlists = cls.youtube.playlistItems().list(**params).execute()
                for item in playlists['items']:
                    video_ids.append(item['snippet']['resourceId'].get('videoId'))
                params['pageToken'] = playlists.get('nextPageToken')
                if not params['pageToken']:
                    break
            except HttpError:
                break
        return video_ids


class Channel:


    def __init__(self, channel_id=None, channel_json=None) -> None:

        if channel_id is not None:
            self.__channel_info = Youtube.get_channel(channel_id=channel_id)
        elif channel_json is not None:
            with open(channel_json, 'r') as file:
                data = file.read()
                self.__channel_info = json.loads(data)
        else:
            raise Exception('Illegal arguments')

        self.__channel_id = channel_id
        self.__title = self.title
        self.__description = self.description
        self.__link = self.link
        self.__subscriber_count = self.subscriber_count
        self.__video_count = self.video_count
        self.__view_count = self.view_count

    def __repr__(self) -> str:
        return f'Channel(channel_id={self.__channel_id})'

    def __str__(self) -> str:
        return f'YouTube-канал: {self.__title}'

    def __len__(self) -> int | None:

        if self.__subscriber_count is not None:
            return self.__subscriber_count
        return 0

    def __add__(self, other: 'Channel') -> int | None:

        if not isinstance(other, Channel):
            raise ArithmeticError('Правый операнд должен быть объектом Channel')
        if self.__subscriber_count is None or other.__subscriber_count is None:
            return None
        return self.__subscriber_count + other.__subscriber_count

    def __gt__(self, other: 'Channel') -> bool | None:

        if not isinstance(other, Channel):
            raise TypeError('Правый операнд должен быть объектом Channel')
        if self.__subscriber_count is None or other.__subscriber_count is None:
            return None
        return self.__subscriber_count > other.__subscriber_count

    @property
    def channel_id(self) -> str | None:

        return self.__channel_id

    @property
    def title(self) -> str | None:

        if self.__channel_info.get('items'):
            channel_title = self.__channel_info.get('items')[0].get('snippet').get('title')
            return channel_title
        return None

    @property
    def description(self) -> str | None:

        if self.__channel_info.get('items'):
            channel_description = self.__channel_info.get('items')[0].get('snippet').get('description')
            return channel_description
        return None

    @property
    def link(self) -> str | None:

        if self.__channel_info.get('items'):
            channel_link = self.__channel_info.get('items')[0].get('snippet').get('customUrl')
            return channel_link
        return None

    @property
    def subscriber_count(self) -> int | None:

        if self.__channel_info.get('items'):
            channel_subscriber = self.__channel_info.get('items')[0].get('statistics').get('subscriberCount')
            return int(channel_subscriber)
        return None

    @property
    def video_count(self) -> int | None:

        if self.__channel_info.get('items'):
            channel_video = self.__channel_info.get('items')[0].get('statistics').get('videoCount')
            return int(channel_video)
        return None

    @property
    def view_count(self) -> int | None:

        if self.__channel_info.get('items'):
            channel_view = self.__channel_info.get('items')[0].get('statistics').get('viewCount')
            return int(channel_view)
        return None

    def print_info(self) -> None:

        print(self.__channel_info)

    def to_json(self) -> None:

        with open(f'{self.__channel_id}.json', 'w', encoding='utf-8') as file:
            json.dump(self.__channel_info, file, indent='\t')


class Video:


    def __init__(self, video_id=None, video_json=None) -> None:

        if video_id is not None:
            self.__video_info = Youtube.get_video(video_id=video_id)
        elif video_json is not None:
            with open(video_json, 'r') as file:
                data = file.read()
                self.__video_info = json.loads(data)
        else:
            raise Exception('Illegal arguments')

        self.__video_id = video_id
        self.__title = self.title
        self.__url = self.url
        self.__view_count = self.view_count
        self.__like_count = self.like_count
        self.__duration = self.duration

    def __repr__(self) -> str:
        return f'Video(video_id={self.__video_id})'

    def __str__(self) -> str:
        return self.__title

    @property
    def video_id(self) -> str:

        return self.__video_id

    @property
    def title(self) -> str | None:

        if self.__video_info.get('items'):
            video_title = self.__video_info.get('items')[0].get('snippet').get('localized').get('title')
            return video_title
        return None

    @property
    def url(self) -> str | None:

        if self.__video_info.get('items'):
            video_id = self.__video_info.get('items')[0].get('id')
            url = f'https://www.youtube.com/watch?v={video_id}'
            return url
        return None

    @property
    def view_count(self) -> int | None:

        if self.__video_info.get('items'):
            view_count = self.__video_info.get('items')[0].get('statistics').get('viewCount')
            return int(view_count)
        return None

    @property
    def like_count(self) -> int | None:

        if self.__video_info.get('items'):
            like_count = self.__video_info.get('items')[0].get('statistics').get('likeCount')
            return int(like_count)
        return None

    @property
    def duration(self) -> str | None:

        if self.__video_info.get('items'):
            iso_8601_duration = self.__video_info.get('items')[0].get('contentDetails').get('duration')
            duration = isodate.parse_duration(iso_8601_duration)
            return duration
        return None


class PLVideo(Video):

    def __init__(self, video_id=None, video_json=None, playlist_id=None, playlist_json=None) -> None:

        super().__init__(video_id, video_json)
        if playlist_id is not None and video_id is not None:
            self.__playlist_info = Youtube.get_video_in_playlist(video_id=video_id, playlist_id=playlist_id)
        elif playlist_json is not None and video_json is not None:
            with open(playlist_json, 'r') as file:
                data = file.read()
                self.__playlist_info = json.loads(data)
        else:
            raise Exception('Illegal arguments')

        self.__id_playlist = self.id_playlist

    @property
    def id_playlist(self) -> str:
        if self.__playlist_info['items']:
            id_playlist = self.__playlist_info.get('items')[0].get('snippet').get('playlistId')
            return id_playlist
        return f'Видео "{self.title}" нет в указанном плейлисте'


class PlayList:


    def __init__(self, playlist_id=None, playlist_json=None) -> None:

        if playlist_id is not None:
            self.__playlist_info = Youtube.get_playlist(playlist_id=playlist_id)
            self.__video_ids = Youtube.get_playlist_video_ids(playlist_id=playlist_id)
        elif playlist_json is not None:
            with open(playlist_json, 'r') as file:
                data = file.read()
                self.__playlist_info = json.loads(data)
                self.__video_ids = None
        else:
            raise Exception('Illegal arguments')

        self.__playlist_id = playlist_id
        self.__title = self.title
        self.__url = self.url

    def __repr__(self) -> str:
        return f'PlayList(playlist_id={self.__playlist_id})'

    def __str__(self) -> str:
        return f'YouTube-плейлист: {self.__title}'

    @property
    def playlist_id(self):

        return self.__playlist_id

    @property
    def title(self) -> str | None:

        if self.__playlist_info.get('items'):
            playlist_title = self.__playlist_info.get('items')[0].get('snippet').get('title')
            return playlist_title
        return None

    @property
    def url(self) -> str | None:

        if self.__playlist_info.get('items'):
            url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'
            return url
        return None

    @property
    def total_duration(self) -> datetime.timedelta:

        print('Подсчитываю длительность...')
        total_duration = datetime.timedelta(seconds=0)
        for video_id in self.__video_ids:
            print('.', end='')
            duration = Video(video_id=video_id).duration
            total_duration += duration
        print('\n')
        return total_duration

    def show_best_video(self) -> str:

        print('Выбираю лучшее видео...')
        max_like_amount = 0
        best_video_url = None
        for video_id in self.__video_ids:
            print('.', end='')
            video = Video(video_id=video_id)
            like_count = video.like_count
            if max_like_amount < like_count:
                max_like_amount = like_count
                best_video_url = video.url
        print('\n')
        return best_video_url