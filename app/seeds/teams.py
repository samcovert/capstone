from app.models import db, Team, environment, SCHEMA
from sqlalchemy.sql import text

def seed_teams():
    team1 = Team(
        year='1996-97',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-1996.png',
        user_id=1
    )

    db.session.add(team1)
    db.session.commit()

def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
