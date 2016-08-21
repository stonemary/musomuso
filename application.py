from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'hi muso'

@application.route('/oauth/')
def print_oauth():
    return str(request.args)

if __name__ == '__main__':
    application.run()
