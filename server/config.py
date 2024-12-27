import os

class Config:
    # Construct the path to the database file dynamically
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getcwd(), 'server', 'instance', 'data.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking