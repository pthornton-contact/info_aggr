from models.base import db

class FeedItem(db.Model):
    __tablename__ = "feed_items"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<FeedItem {self.title}>"