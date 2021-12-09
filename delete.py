from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Delete(MethodView):
    def get(self):
        """
        Accepts GET requests and displays the delete page
        """
        return render_template('delete.html')

    def post(self):
        """
        Accepts DELETE requests, and processes the form;
        Redirect to main when completed.
        """
        model = gbmodel.get_model()
        model.delete(request.form['department'], request.form['courseNum'], request.form['quarter'], request.form['year'], request.form['instructor'])
        return redirect(url_for('main'))

