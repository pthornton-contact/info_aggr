from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Import all models to register them with SQLAlchemy
from .user import User
from .feed_item import FeedItem
from .subscription import Subscription