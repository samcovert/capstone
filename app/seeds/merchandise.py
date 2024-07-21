from app.models import db, Merchandise, environment, SCHEMA
from sqlalchemy.sql import text

def seed_merch():
    merch1 = Merchandise(
        name='Shane Doan Jersey',
        description='Selling my Doaner jersey. Need the cash.',
        price=300,
        user_id=1
    )
    merch2 = Merchandise(
        name='Pacific Division Champions Banner',
        description='This is from 2012 when the yotes won the division. I don\'t have any space for it anymore.',
        price=20,
        user_id=1
    )
    merch3 = Merchandise(
        name='Chris King Signed Picture',
        description='Chris King signed this himself in 1997.',
        price=200,
        user_id=2
    )
    merch4 = Merchandise(
        name='Beat LA Whiteout Shirt',
        description='I got this in the 2012 playoffs when they played LA.',
        price=50,
        user_id=2
    )
    merch5 = Merchandise(
        name='Jeremy Roenick signed stick',
        description='JR signed this stick for me in 1999.',
        price=250,
        user_id=1
    )
    merch6 = Merchandise(
        name='Signed Team Jersey 2000-01',
        description='I got this signed by the whole team in 2001.',
        price = 500,
        user_id=2
    )

    db.session.add(merch1)
    db.session.add(merch2)
    db.session.add(merch3)
    db.session.add(merch4)
    db.session.add(merch5)
    db.session.add(merch6)
    db.session.commit()


def undo_merch():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.merchandise RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM merchandise"))

    db.session.commit()
