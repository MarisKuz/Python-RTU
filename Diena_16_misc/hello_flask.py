from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"Hello User {escape(username)}" # remember we do not trust users :)
    # return 'User %s' % escape(username)