from app import db


class Website(db.Model):
    __tablename__ = 'website'

    id = db.Column(db.BigInteger, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    last_crawled = db.Column(db.DateTime)

