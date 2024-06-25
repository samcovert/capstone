from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_comments():
    com1 = Comment(
        content='This is a great point',
        user_id=1,
        news_id=1
    )
    com2 = Comment(
        content='This is a great memory!',
        user_id=2,
        memory_id=1
    )

    db.session.add(com1)
    db.session.add(com2)
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
