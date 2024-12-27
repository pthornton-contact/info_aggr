from flask import Flask, jsonify
from routes.api_routes import api  # Import the blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db  # Imports all models via models/__init__.py
# Initialize extensions

migrate = Migrate()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the blueprint
    app.register_blueprint(api)

    # Health check route
    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok"}), 200

    return app


# Run the application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)