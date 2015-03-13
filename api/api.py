from flask import Flask
from flask_slack import Slack
from settings import *
from utils import getYoutubeVideoViewCount, \
    getYoutubeChannelSubCount, getYoutubeChannelTotalViews, getFacebookPageLikes

app = Flask(__name__)
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

@slack.command('count', token=YOUTUBE_VIDEO_COUNT_SLACK_TOKEN, team_id=SLACK_TEAM_ID, methods=['POST'])
def viewCount(**kwargs):
    text = getYoutubeVideoViewCount()
    return slack.response(text)


@slack.command('subs', token=YOUTUBE_SUBS_SLACK_TOKEN, team_id=SLACK_TEAM_ID, methods=['POST'])
def subs(**kwargs):
    text = getYoutubeChannelSubCount()
    return slack.response(text)


@slack.command('ccount', token=YOUTUBE_CHANNEL_COUNT_SLACK_TOKEN, team_id=SLACK_TEAM_ID, methods=['POST'])
def totalViews(**kwargs):
    text = getYoutubeChannelTotalViews()
    return slack.response(text)


@slack.command('likes', token=FACEBOOK_SLACK_TOKEN, team_id=SLACK_TEAM_ID, methods=['POST'])
def facebookLikes(**kwargs):
    text = getFacebookPageLikes()
    return slack.response(text)