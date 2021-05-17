from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.email import Email
import re

@app.route("/")
def display():
    return render_template("index.html")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
@app.route("/create", methods = ["POST"])
def create():
    if not Email.validate_email(request.form):
        # redirect to the route where the burger form is rendered.
        print('redirecting line 16')
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        flash("Invalid email address!")
        print('I should be flashing')
        return redirect('/')
    print('I GOT HERE')
    # else no errors:
    email = Email.create(request.form)
    return redirect("success")

@app.route("/success")
def get_emails():
    emails = Email.get_emails()
    return render_template("success.html", emails = emails)
