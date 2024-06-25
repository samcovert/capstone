from .db import db, environment, SCHEMA, add_prefix_for_prod

class Team(db.Model):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String, nullable=False)
    team_name = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    players = db.relationship('Player', back_populates='teams')
    users = db.relationship('User', back_populates='teams')

    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'team_name': self.team_name,
            'logo': self.logo,
            'user_id': self.user_id
        }
