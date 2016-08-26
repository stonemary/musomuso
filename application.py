from flask import Flask, request, redirect
from snspy import APIClient
from snspy import SinaWeiboMixin

application = Flask(__name__)

APP_KEY = ''            # app key
APP_SECRET = '    '      # app secret
CALLBACK_URL = 'http://muso-env.smi9hj2mzt.us-west-2.elasticbeanstalk.com/oauth/'  # callback url

client = APIClient(SinaWeiboMixin, app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)


@application.route('/')
def hello_world():
    return 'hi muso'


@application.route('/oauth/')
def get_access_token():
    code = request.args['code']
    r = client.request_access_token(code)
    access_token = r.access_token
    expires = r.expires
    return 'access_token = {}, expires = {}'.format(access_token, expires)


@application.route('/get_oauth/')
def print_oauth():
    url = client.get_authorize_url()
    return redirect(url)


if __name__ == '__main__':
    application.run()
