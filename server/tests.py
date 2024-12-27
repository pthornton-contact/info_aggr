import unittest
from server.app import create_app
from server.models import db, User, FeedItem

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        # Create app and set testing configuration
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # In-memory database
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        
        self.client = self.app.test_client()

        # Initialize database and create schema
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop all tables and remove session
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_health_check(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_get_users(self):
        # Add a user to the database
        with self.app.app_context():
            db.session.add(User(username="test_user", email="test@example.com"))
            db.session.commit()

        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_add_user(self):
        data = {"username": "new_user", "email": "new_user@example.com"}
        response = self.client.post("/api/users", json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_feed_items(self):
        # Add a feed item to the database
        with self.app.app_context():
            db.session.add(FeedItem(title="Test Feed", url="http://example.com"))
            db.session.commit()

        response = self.client.get("/api/feeds")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_add_feed_item(self):
        data = {"title": "New Feed", "url": "http://example.com"}
        response = self.client.post("/api/feeds", json=data)
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()