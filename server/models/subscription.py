from . import db

class Subscription(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    feed_item_id = db.Column(db.Integer, db.ForeignKey('feed_items.id'), nullable=False)

    user = db.relationship('User', back_populates='subscriptions')
    feed_item = db.relationship('FeedItem', back_populates='subscriptions')