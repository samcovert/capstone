"""create_likes_table

Revision ID: 03f4fc69ceb1
Revises: ffdc0a98111c
Create Date: 2024-07-21 15:27:28.880129

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '03f4fc69ceb1'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_id', sa.Integer(), sa.ForeignKey('news.id', ondelete='CASCADE'), nullable=True),
    sa.Column('memory_id', sa.Integer(), sa.ForeignKey('memories.id', ondelete='CASCADE'), nullable=True),
    sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    )

    if environment == 'production':
        op.execute(f"ALTER TABLE likes SET SCHEMA {SCHEMA};")


def downgrade():
    op.drop_table('likes')
