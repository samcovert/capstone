from .db import db, environment, SCHEMA, add_prefix_for_prod

class Players(db.Model):
    __tablename__ = 'players'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primay_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    number = db.Column(db.integer)
    goals = db.Column(db.integer)
    assists = db.Column(db.integer)
    points = db.Column(db.integer)
    pims = db.Column(db.integer)
    plus_minus = db.Column(db.integer)
    wins = db.Column(db.integer)
    gaa = db.Column(db.integer)
    svp = db.Column(db.integer)
    team_id = db.Column(db.integer, db.ForeignKey(add_prefix_for_prod('teams.id', ondelete='CASCADE')), nullable=False)

    teams = db.relationship('Team', back_populates='players', cascade='all, delete-orphan')

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
            'team_id': self.team_id
        }
