from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from server.config import Config
from server.routes.api_routes import api
from server.models import db  # Imports all models via models/__init__.py

# Initialize extensions
migrate = Migrate()


def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}}) # Replace with your frontend URL if different

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(api)

    # News route
    @app.route("/news")
    def news():
        return render_template('news.html')

    # Health check route
    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok"}), 200

    return app


# Entry point for running the application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)