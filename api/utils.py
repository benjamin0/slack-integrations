from apiclient.discovery import build
from consts import *


def getYoutubeVideoViewCount():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        part="id,snippet",
        type='video',
        channelId=CHANNEL_ID,
        order='date',
        maxResults=1,
    ).execute()

    latestVideoId = search_response['items'][0]['id']['videoId']

    video_response = youtube.videos().list(
        part="snippet,statistics",
        id=latestVideoId,
    ).execute()

    text = '%s views for %s' % (video_response['items'][0]['statistics']['viewCount'],
                                video_response['items'][0]['snippet']['title'])

    return text


def getYoutubeChannelSubCount():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    channel_response = youtube.channels().list(
        part="id,snippet,statistics",
        id=CHANNEL_ID,
        maxResults=1,
    ).execute()

    text = '%s subscribers for %s' % (channel_response['items'][0]['statistics']['subscriberCount'],
                                      channel_response['items'][0]['snippet']['title'])
    return text