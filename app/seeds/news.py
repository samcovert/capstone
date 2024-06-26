from app.models import db, News, environment, SCHEMA
from sqlalchemy.sql import text

def seed_news():
    news1 = News(
        title='MERUELO OUT',
        details='Get this guy out of AZ',
        user_id=2
    )

    db.session.add(news1)
    db.session.commit()


def undo_news():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.news RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM news"))

    db.session.commit()
