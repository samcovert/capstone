from flask import Blueprint, request, jsonify, abort
from app.models import Memory, Image, db
from flask_login import current_user, login_required

memories_bp = Blueprint('memories', __name__)

# GET ALL MEMORIES
@memories_bp.route('/')
def get_mems():
    mems = Memory.query.all()
    return jsonify([mem.to_dict() for mem in mems])

# GET MEMORY DETAILS
@memories_bp.route('/<int:id>/')
def get_mem_by_id(id):
    mem = Memory.query.get_or_404(id)
    return jsonify(mem.to_dict())

# CREATE NEW MEMORY
@memories_bp.route('/new/', methods=['POST'])
@login_required
def create_memory():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    new_mem = Memory(
        title=data.get('title'),
        details=data.get('details'),
        user_id=current_user.id
    )
    db.session.add(new_mem)
    db.session.commit()

    return jsonify(new_mem.to_dict()), 201

# ADD IMAGE TO MEMORY
@memories_bp.route('/new/image/', methods=['POST'])
@login_required
def create_image():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    new_image = Image(
        url=data.get('url'),
        memory_id=data.get('merch_id')
    )
    db.session.add(new_image)
    db.session.commit()
    return jsonify(new_image.to_dict()), 201

# EDIT MEMORY
@memories_bp.route('/<int:id>/edit/', methods=['PUT'])
@login_required
def update_memory(id):
    data = request.get_json
    memory = Memory.query.get_or_404(id)

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    memory.title = data.get('title', memory.title)
    memory.details = data.get('details', memory.details)

    db.session.commit()
    return jsonify(memory.to_dict())

# EDIT IMAGE
@memories_bp.route('/<int:id>/images/edit/', methods=["PUT"])
@login_required
def update_image(id):
    data = request.get_json()
    image = Image.query.get_or_404(id)

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    image.url = data.get('url', image.url)

    db.session.commit()
    return jsonify(image.to_dict())

# DELETE MEMORY
@memories_bp.route('/<int:id>/delete/', methods=['DELETE'])
@login_required
def delete_memory(id):
    memory = Memory.query.get_or_404(id)

    db.session.delete(memory)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})
