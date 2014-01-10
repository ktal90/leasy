# -*- coding: utf-8 -*-
'''Members-only module, typically including the app itself.
'''
from flask import Blueprint, render_template
from leasy.utils import login_required

blueprint = Blueprint('member', __name__,
                        static_folder="../static",
                        template_folder="../templates")

@blueprint.route("/members/")
@login_required
def members():
    return render_template("members.html")
  
@blueprint.route("/payment/")
@login_required
def payment():
    return render_template("payment.html")
  
@blueprint.route("/apartment/")
@login_required
def apartment():
    return render_template("apartment.html")