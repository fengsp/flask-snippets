# -*- coding: utf-8 -*-
"""
    forms.form_from_model
    ~~~~~~~~~~~~~~~~~~~~~

    Automatically create a WTForms Form from model
    http://flask.pocoo.org/snippets/60/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template, url_for, redirect
from flaskext.wtf import Form
from wtforms.ext.appengine.db import model_form
from wtforms import validators

from app import app
from models import MyModel


MyForm = model_form(MyModel, Form, field_args = {
    'name' : {
        'validators' : [validators.Length(max=10)]
    }
})


@app.route("/edit<id>")
def edit(id):
    MyForm = model_form(MyModel, Form)
    model = MyModel.get(id)
    form = MyForm(request.form, model)

    if form.validate_on_submit():
        form.populate_obj(model)
        model.put() 
        flash("MyModel updated")
        return redirect(url_for("index"))
    return render_template("edit.html", form=form)


if __name__ == "__main__":
    app.run()
