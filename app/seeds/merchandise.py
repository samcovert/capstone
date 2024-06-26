from app.models import db, Merchandise, environment, SCHEMA
from sqlalchemy.sql import text

def seed_merch():
    merch1 = Merchandise(
        name='Shane Doan Jersey',
        description='Selling my Doaner jersey. Need the cash.',
        price=300,
        user_id=1
    )

    db.session.add(merch1)
    db.session.commit()


def undo_merch():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.merchandise RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM merchandise"))

    db.session.commit()
