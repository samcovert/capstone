from flask import Blueprint, request, jsonify, abort
from app.models import Memory, db
from flask_login import current_user, login_required

memories_bp = Blueprint('memories', __name__)

# GET ALL MEMORIES
@memories_bp.route('/')
def get_mems():
    mems = Memory.query.all()
    return jsonify([mem.to_dict() for mem in mems])
