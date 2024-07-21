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
    user_likes = db.relationship('Like', back_populates='memories', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'details': self.details,
            'likes': self.likes,
            'user': self.users.to_dict(),
            'comments': [comment.to_dict() for comment in self.comments],
            'images': [image.to_dict() for image in self.images],
            'user_likes': [like.to_dict() for like in self.user_likes]
        }
