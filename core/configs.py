from re import DEBUG
import bcrypt
from dotenv import load_dotenv
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",   #NOTE Blue
        "INFO": "\033[92m",    #NOTE  Green 
        "WARNING": "\033[93m", #NOTE Yellow
        "ERROR": "\033[91m",   #NOTE Red
        "CRITICAL": "\033[1;91m", # Bold Red
    }
    RESET = "\033[0m"

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{log_color}{record.levelname}{self.RESET}"
        return super().format(record)


logger = logging.getLogger("colored_logger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter("%(levelname)s:     %(funcName)s:Line-%(lineno)d: %(message)s"))
# Add handler to logger
logger.addHandler(handler)
bcrypt = Bcrypt()


load_dotenv()

class Config:
    """Base config class."""
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
