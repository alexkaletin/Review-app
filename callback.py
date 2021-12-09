from flask import redirect, request, url_for, session
from requests_oauthlib import OAuth2Session
from flask.views import MethodView
from oauth_config import client_id, client_secret, token_url, callback_url

class Callback(MethodView):
    def get(self):
        """
        Steps 6 and 7
        The user visits the callback url with the one-time code attached
        My app then sends the one-time code back to google. By presenting this code, Google can now safely issue an access token to my app that provides it access to the users information for use in the submit page.
        """

        google = OAuth2Session(client_id, redirect_uri=callback_url, state=session['oauth_state'])
        token = google.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)

        #Saves token for it to be a persisted token
        session['oauth_token'] = token

        return redirect(url_for('submit'))
