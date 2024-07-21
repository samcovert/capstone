from .db import db, environment, SCHEMA, add_prefix_for_prod

class News(db.Model):
    __tablename__ = 'news'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    comments = db.relationship('Comment', back_populates='news', cascade='all, delete-orphan')
    users = db.relationship('User', back_populates='news')
    user_likes = db.relationship('Like', back_populates='news', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'details': self.details,
            'likes': self.likes,
            'users': self.users.to_dict(),
            'comments': [comment.to_dict() for comment in self.comments],
            'user_likes': [like.to_dict() for like in self.user_likes]
        }
