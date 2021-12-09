from flask import render_template
from flask.views import MethodView

class Main(MethodView):
    def get(self):
       """
       Accepts GET requests and displays the main page
       """
       return render_template('main.html')
