from .db import db, environment, SCHEMA, add_prefix_for_prod

class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    merch_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('merchandise.id'), ondelete='CASCADE'))
    memory_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('memories.id'), ondelete='CASCADE'))

    merchandise = db.relationship('Merchandise', back_populates='images', foreign_keys=[merch_id])
    memories = db.relationship('Memory', back_populates='images', foreign_keys=[memory_id])

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'merch_id': self.merch_id,
            'memory_id': self.memory_id
        }
