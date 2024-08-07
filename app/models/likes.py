from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import event
from .news import News
from .memories import Memory

class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('news.id'), ondelete='CASCADE'), nullable=True)
    memory_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('memories.id'), ondelete='CASCADE'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    news = db.relationship('News', back_populates='user_likes')
    memories = db.relationship('Memory', back_populates='user_likes')
    user = db.relationship('User', back_populates='likes')


    def to_dict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'memory_id': self.memory_id,
            'news_id': self.news_id
        }


@event.listens_for(Like, 'after_insert')
def after_insert(mapper, connection, target):
    if target.news_id:
        connection.execute(
            News.__table__.update().
            where(News.id == target.news_id).
            values(likes=News.likes + 1)
        )
    elif target.memory_id:
        connection.execute(
            Memory.__table__.update().
            where(Memory.id == target.memory_id).
            values(likes=Memory.likes + 1)
        )


@event.listens_for(Like, 'after_delete')
def after_delete(mapper, connection, target):
    if target.news_id:
        connection.execute(
            News.__table__.update().
            where(News.id == target.news_id).
            values(likes=News.likes - 1)
        )
    elif target.memory_id:
        connection.execute(
            Memory.__table__.update().
            where(Memory.id == target.memory_id).
            values(likes=Memory.likes - 1)
        )
