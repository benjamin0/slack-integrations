import os
from flask import Flask
from flask_slack import Slack
from apiclient.discovery import build

DEVELOPER_KEY = os.environ['DEVELOPER_KEY']
CHANNEL_ID = os.environ['CHANNEL_ID']
TOKEN = os.environ['TOKEN']
TEAM_ID = os.environ['TEAM_ID']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

app = Flask(__name__)
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

@slack.command('count', token=TOKEN, team_id=TEAM_ID, methods=['POST'])
def viewCount(**kwargs):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        part="id,snippet",
        type='video',
        channelId=CHANNEL_ID,
        order='date',
        maxResults=1,
    ).execute()

    latestVideoId = search_response['items'][-1]['id']['videoId']

    video_response = youtube.videos().list(
        part="statistics",
        id=latestVideoId,
    ).execute()

    text = '%s views' % video_response['items'][0]['statistics']['viewCount']
    return slack.response(text)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')