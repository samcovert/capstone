from app.models import db, News, environment, SCHEMA
from sqlalchemy.sql import text

def seed_news():
    news1 = News(
        title='MERUELO OUT',
        details='Get this guy out of AZ',
        user_id=2
    )
    news2 = News(
        title='He is finally gone!',
        details='I cannot believe Meruelo is finally gone!! What a day for the Yotes!!!',
        user_id=1
    )
    news3 = News(
        title='Vejmelka jersey',
        details='Does anybody have a Karel Vejmelka jersey I can buy? He was favorite coyote...',
        user_id=1
    )
    news4 = News(
        title='Sun Belt Stanley Cup',
        details='Congrats to the Panthers on winning the cup. Great to see a sunbelt team get some love!',
        user_id=3
    )

    db.session.add(news1)
    db.session.add(news2)
    db.session.add(news3)
    db.session.add(news4)
    db.session.commit()


def undo_news():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.news RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM news"))

    db.session.commit()
