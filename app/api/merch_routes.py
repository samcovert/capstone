from flask import Blueprint, request, jsonify, abort
from app.models import Merchandise, db
from flask_login import current_user, login_required

merchandise_bp = Blueprint('merch', __name__)

# GET ALL MERCH
@merchandise_bp.route('/')
def get_merch():
    merchandise = Merchandise.query.all()
    return jsonify([merch.to_dict() for merch in merchandise])

# GET MERCH BY ID
@merchandise_bp.route('/<int:id>/')
def get_merch_by_id(id):
    merch = Merchandise.query.get_or_404(id)
    return jsonify(merch.to_dict())

# CREATE NEW MERCH ITEM
@merchandise_bp.route('/new/', methods=["POST"])
@login_required
def create_merch():
    data = request.get_json()

    if not data:
        abort(400, description="Invalid data")

    new_item = Merchandise(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        user_id=current_user.id
    )

    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.to_dict()), 201
