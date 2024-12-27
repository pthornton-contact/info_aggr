from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/feeds', methods=['GET'])
def get_feeds():
    return jsonify({"feeds": ["Feed 1", "Feed 2", "Feed 3"]})