from flask import Blueprint, request, jsonify, abort
from app.models import Memory, db
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
