from flask import Blueprint, request, jsonify
from server.models import db
from server.models.user import User
from server.models.feed_item import FeedItem
from server.models.subscription import Subscription

api = Blueprint('api', __name__)

# Mock response for /api/health
@api.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

# User routes
@api.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@api.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# FeedItem routes
@api.route('/api/feeds', methods=['GET'])
def get_feeds():
    feeds = FeedItem.query.all()
    return jsonify([feed.to_dict() for feed in feeds])

@api.route('/api/feeds', methods=['POST'])
def create_feed():
    data = request.json
    feed = FeedItem(title=data['title'], url=data['url'], description=data.get('description'))
    db.session.add(feed)
    db.session.commit()
    return jsonify(feed.to_dict()), 201

# Subscription routes
@api.route('/api/users/<int:user_id>/subscriptions', methods=['GET'])
def get_user_subscriptions(user_id):
    user = User.query.get_or_404(user_id)
    subscriptions = [
        subscription.feed_item.to_dict() for subscription in user.subscriptions
    ]
    return jsonify(subscriptions)

@api.route('/api/users/<int:user_id>/subscriptions', methods=['POST'])
def subscribe_user_to_feed(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    feed = FeedItem.query.get_or_404(data['feed_id'])
    subscription = Subscription(user=user, feed_item=feed)
    db.session.add(subscription)
    db.session.commit()
    return jsonify(subscription.to_dict()), 201