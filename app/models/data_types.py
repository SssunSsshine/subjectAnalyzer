from app import db


class DataTypes(db.Model):
    __tablename__ = 'data_types'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
