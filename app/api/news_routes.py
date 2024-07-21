from flask import Blueprint, request, jsonify, abort
from app.models import News, Comment, Likes, db
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
    news.likes = data.get('likes', news.likes)

    db.session.commit()
    return jsonify(news.to_dict())

# DELETE NEWS
@news_bp.route('/<int:id>/delete/', methods=['DELETE'])
@login_required
def delete_news(id):
    news = News.query.get_or_404(id)

    db.session.delete(news)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"})

# ADD COMMENT
@news_bp.route('/comment/new/', methods=["POST"])
@login_required
def add_comment():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    new_comment = Comment(
        content=data.get('content'),
        user_id=current_user.id,
        news_id=data.get('news_id')
    )
    db.session.add(new_comment)
    db.session.commit()

    return jsonify(new_comment.to_dict()), 201

# EDIT COMMENT
@news_bp.route('/<int:id>/comment/edit/', methods=['PUT'])
@login_required
def edit_comment(id):
    data = request.get_json()
    comment = Comment.query.get_or_404(id)

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    comment.content = data.get('content', comment.content)
    db.session.commit()
    return jsonify(comment.to_dict())

# DELETE COMMENT
@news_bp.route('/<int:id>/comment/delete/', methods=["DELETE"])
@login_required
def delete_comment(id):
    comment = Comment.query.get_or_404(id)

    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully"})

# ADD LIKE
@news_bp.route('/<int:id>/like/', methods=['POST'])
@login_required
def add_like(id):
    news = News.query.get(id)
    if not news:
        return jsonify({'message': 'News not found'}), 404

    existing_like = Likes.query.filter_by(news_id=id, user_id=current_user.id).first()
    if existing_like:
        return jsonify({'message': 'You already liked this post'}), 400

    like = Likes(
        news_id=id,
        user_id=current_user.id
    )
    db.session.add(like)
    db.session.commit()

    return jsonify(news.to_dict())

# REMOVE LIKE
@news_bp.route('/<int:id>/like/delete/', methods=['DELETE'])
@login_required
def remove_like(id):
    like = Likes.query.get(id)

    db.session.delete(like)
    db.session.commit()
    return jsonify({"message": "Like deleted successfully"})
