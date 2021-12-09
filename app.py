"""
A simple course review flask app.
"""
import flask
import os
from flask.views import MethodView
from main import Main
from index import Index
from submit import Submit
from delete import Delete
from callback import Callback
from logout import Logout

app = flask.Flask(__name__)       # our Flask app

#creates rule for routing to the main page, and which request it has
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])

#creates rule for routing to the index page, and which request it has
app.add_url_rule('/index',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

#creates rule for routing to the submit page, and which request it has
app.add_url_rule('/submit',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

#creates rule for routing to the delete page, and which request it has
app.add_url_rule('/delete',
                 view_func=Delete.as_view('delete'),
                 methods=['GET', 'POST'])

#creates rule for routing to the callback page, and which request it has
app.add_url_rule('/callback',
                 view_func=Callback.as_view('callback'),
                 methods=["GET"])

#creates rule for routing to the logout page, and which request it has
app.add_url_rule('/logout',
                 view_func=Logout.as_view('logout'),
                 methods=["GET"])

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1" #needed if we dont have https
app.secret_key = os.urandom(24)
#app.secret_key = 'secret_random_key'

#The bottom will only run during a python call.
#When run directly by python, uses the run() method of flask to
#lauch the web app on all ip address of the host using port 5000
if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1" #needed if we dont have https
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)
