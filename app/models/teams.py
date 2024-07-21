from .db import db, environment, SCHEMA, add_prefix_for_prod

class Team(db.Model):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String, nullable=False)
    team_name = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    record = db.Column(db.String, nullable=False)
    playoffs = db.Column(db.String, nullable=False)
    coach = db.Column(db.String, nullable=False)

    players = db.relationship('Player', back_populates='teams')

    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'team_name': self.team_name,
            'logo': self.logo,
            'players': [player.to_dict() for player in self.players],
            'record': self.record,
            'playoffs': self.playoffs,
            'coach': self.coach
        }
