from flask import Blueprint, request, jsonify, abort
from app.models import Merchandise, Image, db
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

# ADD IMAGE TO ITEM
@merchandise_bp.route('/new/image/', methods=["POST"])
@login_required
def create_image():
    data = request.get_json()

    if not data:
        abort(400, description="Invalid data")

    new_image = Image(
        url=data.get('url'),
        merch_id=data.get('merch_id')
    )
    db.session.add(new_image)
    db.session.commit()
    return jsonify(new_image.to_dict()), 201

# EDIT ITEM
@merchandise_bp.route('/<int:id>/edit/', methods=["PUT"])
@login_required
def update_item(id):
    data = request.get_json()
    item = Merchandise.query.get_or_404(id)

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)

    db.session.commit()
    return jsonify(item.to_dict())

# EDIT IMAGE
@merchandise_bp.route('/<int:id>/images/edit/', methods=["PUT"])
@login_required
def update_image(id):
    data = request.get_json()
    image = Image.query.get_or_404(id)

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    image.url = data.get('url', image.url)

    db.session.commit()
    return jsonify(image.to_dict())

# DELETE ITEM
@merchandise_bp.route('/<int:id>/delete/', methods=["DELETE"])
def delete_item(id):
    item = Merchandise.query.get_or_404(id)

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})
