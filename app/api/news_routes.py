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


# CREATE NEW NEWS
@news_bp.route('/new/', methods=['POST'])
@login_required
def create_news():
    data = request.get_json()

    if not data:
        abort(400, description='Invalid Data')

    new_news = News(
        title=data.get('title'),
        details=data.get('details'),
        user_id=current_user.id
    )

    db.session.add(new_news)
    db.session.commit()

    return jsonify(new_news.to_dict()), 201

# EDIT NEWS
@news_bp.route('/<int:id>/edit/', methods=['PUT'])
@login_required
def update_news(id):
    data = request.get_json()
    news = News.query.get_or_404(id)

    if not data:
        abort(400, description='Invalid Data')

    news.title = data.get('title', news.title)
    news.details = data.get('details', news.details)

    db.session.commit()
    return jsonify(news.to_dict())
