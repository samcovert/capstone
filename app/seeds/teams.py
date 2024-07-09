from app.models import db, Team, environment, SCHEMA
from sqlalchemy.sql import text

def seed_teams():
    team1 = Team(
        year='1996-97',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-1996.png',
        record='38-37-7',
        playoffs='Lost in round 1',
        coach='Don Hay'
    )
    team2 = Team(
        year='1997-98',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-1996.png',
        record='35-35-12',
        playoffs='Lost in round 1',
        coach='Jim Schoenfield'
    )
    team3 = Team(
        year='1998-99',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-1996.png',
        record='39-31-12',
        playoffs='Lost in round 1',
        coach='Jim Schoenfield'
    )

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)
    db.session.commit()

def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
