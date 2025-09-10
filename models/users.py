from sqlalchemy.orm import mapped_column,Mapped,validates
from sqlalchemy import String
from core.database import db
from core.configs import bcrypt
from flask_login import UserMixin
from datetime import datetime

class User(db.Model,UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str] = mapped_column(String(500), nullable=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at:Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at:Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)
    is_active:Mapped[bool] = mapped_column(default=True,nullable=False)
    verified:Mapped[bool] = mapped_column(default=False,nullable=False)


    @validates('password')
    def hash_password(self, key, value:str):
        if value and not value.startswith('$2b$'):
            return bcrypt.generate_password_hash(value).decode('utf-8')
        return value