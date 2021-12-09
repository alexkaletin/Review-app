from flask import redirect, request, url_for, render_template, session
from flask.views import MethodView
import gbmodel
from requests_oauthlib import OAuth2Session
from oauth_config import client_id, authorization_base_url, callback_url

class Submit(MethodView):
    def get(self):
        """
        Accepts GET requests and displays the submit page
        """
        # If client has an OAuth2 token, use it to get their information and render
        #   the submit page with it
        if 'oauth_token' in session:
            google = OAuth2Session(client_id, token=session['oauth_token'])
            userinfo = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
            return render_template('submit.html', name=userinfo['name'], email=userinfo['email'], picture=userinfo['picture'])
        else:
        # Redirect to the identity provider and ask the identity provider to return the client
        #   back to /callback route with the code
        # If OAuth token not present, start OAuth flow
            google = OAuth2Session(client_id,
                    redirect_uri = callback_url,
                    scope = 'https://www.googleapis.com/auth/userinfo.email ' +                   
                            'https://www.googleapis.com/auth/userinfo.profile'
            )
            authorization_url, state = google.authorization_url(authorization_base_url)

            # Identity provider returns URL and random "state" that must be echoed later to prevent CSRF.
            session['oauth_state'] = state
            return redirect(authorization_url)

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to main when completed.
        """
        #Checks to see if user is logged in, if not redirects back to signin page
        if 'oauth_token' in session:
            model = gbmodel.get_model()
            model.insert(request.form['department'], request.form['courseNum'], request.form['quarter'], request.form['year'], request.form['instructor'], request.form['review'])
            return redirect(url_for('main'))
        else:
            return redirect(url_for('submit'))
