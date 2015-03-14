import facebook
from apiclient.discovery import build
from settings import *

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=YOUTUBE_DEVELOPER_KEY)


def getYoutubeChannel():
    channel_response = youtube.channels().list(
        part="id,snippet,statistics",
        id=YOUTUBE_CHANNEL_ID,
        maxResults=1,
    ).execute()
    return channel_response


def getYoutubeVideoViewCount():
    search_response = youtube.search().list(
        part="id,snippet",
        type='video',
        channelId=YOUTUBE_CHANNEL_ID,
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
    channel_response = getYoutubeChannel()
    text = '%s subscribers for %s' % (channel_response['items'][0]['statistics']['subscriberCount'],
                                      channel_response['items'][0]['snippet']['title'])
    return text


def getYoutubeChannelTotalViews():
    channel_response = getYoutubeChannel()
    text = '%s total views for %s' % (channel_response['items'][0]['statistics']['viewCount'],
                                      channel_response['items'][0]['snippet']['title'])
    return text


def getFacebookPageLikes():
    graph = facebook.GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN)
    page = graph.get_object(id=FACEBOOK_PAGE_ID)
    text = '%s Facebook likes for %s' % (page['likes'], page['name'])
    return text


def getAllStats():
    facebookLikesText = getFacebookPageLikes()
    videoViewsText = getYoutubeVideoViewCount()
    channel_response = getYoutubeChannel()

    subsText = '%s subscribers for %s' % (channel_response['items'][0]['statistics']['subscriberCount'],
                                          channel_response['items'][0]['snippet']['title'])

    channelViewsText = '%s total views for %s' % (channel_response['items'][0]['statistics']['viewCount'],
                                                  channel_response['items'][0]['snippet']['title'])

    allText = '%s\n%s\n%s\n%s' % (subsText, channelViewsText, facebookLikesText, videoViewsText)

    return allText
