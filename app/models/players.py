from .db import db, environment, SCHEMA, add_prefix_for_prod

class Player(db.Model):
    __tablename__ = 'players'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    points = db.Column(db.Integer)
    pims = db.Column(db.Integer)
    plus_minus = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    gaa = db.Column(db.Integer)
    svp = db.Column(db.Integer)
    gp = db.Column(db.Integer)
    age = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id'), ondelete='CASCADE'), nullable=False)

    teams = db.relationship('Team', back_populates='players', cascade='all, delete-orphan', single_parent=True)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'position': self.position,
            'number': self.number,
            'goals': self.goals,
            'assists': self.assists,
            'points': self.points,
            'pims': self.pims,
            'plus_minus': self.plus_minus,
            'wins': self.wins,
            'gaa': self. gaa,
            'svp': self.svp,
            'gp': self.gp,
            'age': self.age,
            'team_id': self.team_id
        }
