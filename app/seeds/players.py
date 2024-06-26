from app.models import db, Player, environment, SCHEMA
from sqlalchemy.sql import text

def seed_players():
    player1 = Player(
        first_name='Shane',
        last_name='Doan',
        position='Forward',
        number=19,
        goals=4,
        assists=8,
        points=12,
        pims=49,
        plus_minus=-3,
        team_id=1
    )

    db.session.add(player1)
    db.session.commit()

def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM players"))

    db.session.commit()
