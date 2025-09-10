import psycopg2
import os

def get_conn():
    conn = psycopg2.connect(
    host = os.environ.get("DB_HOST"),
    database= os.environ.get("DB_DATABASE"),
    user= os.environ.get("DB_USER"),
    password= os.environ.get("DB_PASSWORD"),
    port=os.environ.get("DB_PORT")
    )
    return conn

def init_db():
    conn = get_conn()