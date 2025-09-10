from models.users import User
from flask_login import LoginManager

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id:int):
    user =User.query.get(user_id)
    if user and user.is_active:
        return user
    return None