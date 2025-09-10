import os

from flask import Flask, request, render_template, session, jsonify, flash
import bcrypt
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def landing_page():
    return jsonify(greetings="Hello Everyone Let's get Started")

@app.route("/register")
def register():
    if request.method == "POST":
        firstname = request.form.get("firstname", "").strip()
        lastname = request.form.get("lastname", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()



    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)