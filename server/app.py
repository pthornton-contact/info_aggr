from flask import Flask, jsonify
from routes.api_routes import api  # Import the blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(api)

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200
if __name__ == "__main__":
    app.run(debug=True)
