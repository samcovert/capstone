from flask import Blueprint, request, jsonify, abort
from app.models import Team, Player, db
from flask_login import current_user, login_required

history_bp = Blueprint('history', __name__)

# GET ALL TEAMS
@history_bp.route('/teams/')
def get_teams():
    teams = Team.query.all()
    return jsonify([team.to_dict() for team in teams])

# GET TEAM DETAILS
@history_bp.route('/teams/<string:year>/')
def get_team_details(year):
    team = Team.query.filter_by(year=year).first_or_404()
    return jsonify(team.to_dict())
