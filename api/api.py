from flask import Flask
from flask_slack import Slack
from consts import *
from utils import getYoutubeVideoViewCount

app = Flask(__name__)
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

@slack.command('count', token=COUNT_TOKEN, team_id=TEAM_ID, methods=['POST'])
def viewCount(**kwargs):
    text = getYoutubeVideoViewCount()
    return slack.response(text)