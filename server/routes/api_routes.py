from flask import Blueprint, request, jsonify
from server.models import db
from server.models.user import User
from server.models.feed_item import FeedItem
from server.models.subscription import Subscription
from server.models.research_paper import ResearchPaper
from server.models.stock_data import StockData
api = Blueprint('api', __name__)

# Mock response for /api/health
@api.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

# User routes
@api.route('/api/feeds', methods=['GET'])
def get_feeds():
    stocks = StockData.query.all()
    papers = ResearchPaper.query.all()

    feed_items = []

    # Convert stock_data rows to feed-friendly dicts
    for stock in stocks:
        feed_items.append({
            'type': 'stock',
            'id': stock.id,
            'ticker': stock.ticker,         # rename from 'symbol' -> 'ticker'
            'price': stock.close_price,     # rename from 'price' -> one of your float fields
            'timestamp': stock.timestamp,   
        })

    # Convert research_papers rows to feed-friendly dicts
    for paper in papers:
        feed_items.append({
            'type': 'research',
            'id': paper.id,
            'title': paper.title,
            'abstract': paper.abstract,
            'published_date': paper.published_date,
        })

    feed_items.sort(
        key=lambda item: item.get('timestamp') or item.get('published_date'), 
        reverse=True
    )

    return jsonify(feed_items)

@api.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201



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