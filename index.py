from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        """
        Accepts GET requests and displays the index page
        """
        model = gbmodel.get_model()
        entries = [dict(department=row[0], courseNum=row[1], quarter=row[2], year=row[3] , instructor=row[4], review=row[5], translated=row[6]) for row in model.select()]
        return render_template('index.html',entries=entries)
