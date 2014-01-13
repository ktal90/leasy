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
  
@blueprint.route("/payments/")
@login_required
def payments():
    return render_template("payments.html")
  
@blueprint.route("/maintenance/")
@login_required
def maintenance():
    return render_template("maintenance.html")

@blueprint.route("/split/")
@login_required
def split():
    return render_template("split.html")