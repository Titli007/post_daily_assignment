from flask import Blueprint, request, jsonify
from controllers.news_controller import news_controller

# Create a Blueprint for news routes
news_bp = Blueprint('news', __name__)

@news_bp.route('/news', methods=['POST'])
def news():
    return news_controller()
