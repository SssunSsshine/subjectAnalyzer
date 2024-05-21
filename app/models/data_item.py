from app import db


class DataItem(db.Model):
    __tablename__ = 'data_item'

    id = db.Column(db.BigInteger, primary_key=True)
    page_id = db.Column(db.BigInteger, db.ForeignKey('page.id', ondelete='CASCADE'), nullable=False)
    data_type_id = db.Column(db.BigInteger, db.ForeignKey('data_types.id'), nullable=False)
    data_value = db.Column(db.Text, nullable=False)
