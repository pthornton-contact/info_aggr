import os

class Config:
    # Construct the path to the database file dynamically
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getcwd(), 'server', 'instance', 'data.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    CELERY_BROKER_URL = "redis://localhost:6379/0"  # Broker
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"  # Result backend