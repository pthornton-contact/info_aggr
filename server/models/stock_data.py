from server.models import db

class StockData(db.Model):
    __tablename__ = 'stock_data'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

