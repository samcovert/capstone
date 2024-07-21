from app.models import db, Like, environment, SCHEMA
from sqlalchemy.sql import text

def seed_likes():
    like1 = Like(
        news_id=1,
        user_id=1
    )
    like2 = Like(
        news_id=2,
        user_id=2
    )
    like3 = Like(
        news_id=2,
        user_id=3
    )
    like4 = Like(
        news_id=3,
        user_id=2
    )
    like5 = Like(
        news_id=3,
        user_id=3
    )
    like6 = Like(
        memory_id=1,
        user_id=2
    )
    like7 = Like(
        memory_id=2,
        user_id=1
    )
    like8 = Like(
        memory_id=3,
        user_id=1
    )

    db.session.add(like1)
    db.session.add(like2)
    db.session.add(like3)
    db.session.add(like4)
    db.session.add(like5)
    db.session.add(like6)
    db.session.add(like7)
    db.session.add(like8)

    db.session.commit()

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM likes"))

    db.session.commit()
