# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)
from sqlalchemy.exc import IntegrityError

from leasy.models import User
from leasy.forms import RegisterForm, LoginForm
from leasy.utils import flash_errors
from leasy.models import db

blueprint = Blueprint('public', __name__,
                        static_folder="../static",
                        template_folder="../templates")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    if request.method == 'POST':
        u = User.query.filter_by(email=request.form['email'],
                                password=request.form['password']).first()
        if u is None:
            error = 'Invalid email or password.'
            flash(error, 'warning')
        else:
            session['logged_in'] = True
            session['email'] = u.email
            session['firstname'] = u.firstname
            flash("You are logged in.", 'success')
            return redirect(url_for("member.members"))
    return render_template("home.html", form=form)

@blueprint.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))

@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Thank you for registering. You can now log in.", 'success')
            return redirect(url_for('public.home'))
        except IntegrityError as err:
            print(err)
            flash("An account with that email address already exists. Try again.", 'warning')
    else:
        flash_errors(form)
    return render_template('register.html', form=form)

@blueprint.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("about.html", form=form)

@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404