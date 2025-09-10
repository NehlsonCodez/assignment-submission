import os
from sys import prefix
from flask import Flask, request, render_template,jsonify, flash
from core.configs import Config,bcrypt,logger
from services.user import login_manager
from core.database import db
from blueprints.user import user_bp
from blueprints.auth import auth_bp
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = Config.SECRET_KEY
    logger.info("Initializing Flask extensions...")
    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    logger.info("Attempting to connect to the database...")
    with app.app_context():
        db.create_all()
        logger.info("Database connected and tables created if not exist.")
    login_manager.login_view = 'auth.login'  # type: ignore
    return app

app = create_app()
app.register_blueprint(user_bp,url_prefix="/user")
app.register_blueprint(auth_bp,url_prefix="/auth")

@app.route("/")
def landing_page():
    return jsonify(greetings="Hello Everyone Let's get Started")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=Config.DEBUG)