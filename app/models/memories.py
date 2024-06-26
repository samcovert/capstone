from .db import db, environment, SCHEMA, add_prefix_for_prod

class Memory(db.Model):
    __tablename__ = 'memories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    comments = db.relationship('Comment', back_populates='memories', cascade='all, delete-orphan')
    images = db.relationship('Image', back_populates='memories')
    users = db.relationship('User', back_populates='memories')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'details': self.details,
            'likes': self.likes,
            'user_id': self.user_id
        }
