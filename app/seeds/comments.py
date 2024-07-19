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
    com3 = Comment(
        content='He needs to go',
        user_id=3,
        news_id=1
    )
    com4 = Comment(
        content='Best day of my life',
        user_id=3,
        news_id=2
    )
    com5 = Comment(
        content='I have one but you can\'t have it. sorry',
        user_id=3,
        news_id=3
    )
    com6 = Comment(
        content='I have one! I\'ll post it on the store!',
        user_id=2,
        news_id=3
    )
    com7 = Comment(
        content='I agree bobbie but is he our fastest path to getting hockey back in AZ?',
        user_id=2,
        news_id=1
    )
    com8 = Comment(
        content='I really dont care if he is marnie. He doesnt deserve a team',
        user_id=3,
        news_id=1
    )
    com9 = Comment(
        content='love to see OEL get a cup too',
        user_id=1,
        news_id=4
    )

    db.session.add(com1)
    db.session.add(com2)
    db.session.add(com3)
    db.session.add(com4)
    db.session.add(com5)
    db.session.add(com6)
    db.session.add(com7)
    db.session.add(com8)
    db.session.add(com9)

    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
