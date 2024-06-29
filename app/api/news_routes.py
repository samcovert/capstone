from flask import Blueprint, request, jsonify, abort
from app.models import News, db
from flask_login import current_user, login_required

news_bp = Blueprint('news', __name__)

# GET ALL NEWS
@news_bp.route('/')
def get_news():
    news = News.query.all()
    return jsonify([posts.to_dict() for posts in news])

# GET NEWS BY ID
@news_bp.route('/<int:id>/')
def get_news_by_id(id):
    news = News.query.get_or_404(id)
    return jsonify(news.to_dict())
