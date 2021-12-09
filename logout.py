from flask import redirect, url_for, session
from flask.views import MethodView

class Logout(MethodView):
    def get(self):
        """
        Accepts GET requests and clears the user sesssion and redirects to main page.
        """
        session.clear()
        return redirect(url_for('main'))
