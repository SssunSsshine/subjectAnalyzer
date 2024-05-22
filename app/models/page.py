from app import db


class Page(db.Model):
    __tablename__ = 'page'

    id = db.Column(db.BigInteger, primary_key=True)
    webside_id = db.Column(db.BigInteger, db.ForeignKey('website.id', ondelete='CASCADE'), nullable=False)
    url = db.Column(db.String(255), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    crawled_at = db.Column(db.DateTime)
