from .db import db, environment, SCHEMA, add_prefix_for_prod

class Merchandise(db.Model):
    __tablename__ = 'merchandise'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), ondelete='CASCADE'), nullable=False)

    users = db.relationship('User', back_populates='merchandise')
    images = db.relationship('Image', back_populates='merchandise')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'user_id': self.user_id,
        }
