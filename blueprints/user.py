from flask import Blueprint, render_template, session, redirect, url_for, flash
from models.users import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/user/show")
def user_show():
    user_id = session.get("user_id")
    if not user_id:
        flash("Please sign in to view your profile.")
        return redirect(url_for("auth.login"))
    user = User.query.get(user_id)
    return render_template("user_show.html", user=user)
