from . import db

class FeedItem(db.Model):
    __tablename__ = 'feed_items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)

    subscriptions = db.relationship('Subscription', back_populates='feed_item')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "description": self.description,
            "subscriptions": [subscription.user_id for subscription in self.subscriptions],
        }