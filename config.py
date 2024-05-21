import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/web_crawler'
    SECRET_KEY = os.urandom(24)
