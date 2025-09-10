from asyncio import log
from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models.users import User
from core.database import db
from core.configs import bcrypt,logger
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint("auth", __name__)


# Signup route
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        full_name = request.form.get("full_name", "")
        bio = request.form.get("bio", "")
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("auth.signup"))
        if User.query.filter_by(email=email).first():
            flash("Email already exists")
            return redirect(url_for("auth.signup"))
        user = User(
            username=username,  # type: ignore
            email=email,  # type: ignore
            password=password,  # type: ignore
            full_name=full_name,  # type: ignore
            bio=bio,  # type: ignore
        )
        db.session.add(user)
        db.session.commit()
        logger.info(f"New user registered: {username}")
        flash("Account created! Please sign in.")
        return redirect(url_for("auth.login"))
    return render_template("register.html")


# Login route
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user: User = User.query.filter_by(username=username).first()  # type: ignore
        if user and bcrypt.check_password_hash(user.password, password):
            logger.info(f"User {username} logged in successfully.")
            login_user(user)
        flash("Invalid credentials")
        return redirect(url_for("auth.login"))
    return render_template("login.html")


# Reset password route
@auth_bp.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Email not found")
            return redirect(url_for("auth.reset_password"))
        new_password = request.form["new_password"]
        user.password = bcrypt.generate_password_hash(new_password).decode("utf-8")
        db.session.commit()
        flash("Password reset successful!")
        return redirect(url_for("auth.login"))
    return render_template("reset_password.html")


# Logout route
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for("auth.login"))
