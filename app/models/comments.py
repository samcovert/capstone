from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)
    memory_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('memories.id'), ondelete='CASCADE'))
    news_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('news.id'), ondelete='CASCADE'))

    users = db.relationship('User', back_populates='comments')
    memories = db.relationship('Memory', back_populates='comments')
    news = db.relationship('News', back_populates='comments')

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'memory_id': self.memory_id,
            'news_id': self.news_id
        }
