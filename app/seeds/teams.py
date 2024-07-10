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
    team4 = Team(
        year='1999-00',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-99-03.png',
        record='39-31-12',
        playoffs='Lost in round 1',
        coach='Bob Francis'
    )
    team5 = Team(
        year='2000-01',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-99-03.png',
        record='35-27-20',
        playoffs='Missed playoffs',
        coach='Bob Francis'
    )
    team6 = Team(
        year='2001-02',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-99-03.png',
        record='40-27-12',
        playoffs='Lost in first round',
        coach='Bob Francis'
    )
    team7 = Team(
        year='2002-03',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-99-03.png',
        record='31-35-17',
        playoffs='Missed playoffs',
        coach='Bob Francis'
    )
    team8 = Team(
        year='2003-04',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='22-26-23',
        playoffs='Missed playoffs',
        coach='Bob Francis, Rick Bowness'
    )
    team9 = Team(
        year='2005-06',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='38-39-5',
        playoffs='Missed playoffs',
        coach='Wayne Gretzky'
    )
    team10 = Team(
        year='2006-07',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='31-46-5',
        playoffs='Missed playoffs',
        coach='Wayne Gretzky'
    )
    team11 = Team(
        year='2007-08',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='38-37-7',
        playoffs='Missed playoffs',
        coach='Wayne Gretzky'
    )
    team12 = Team(
        year='2008-09',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='36-39-7',
        playoffs='Missed playoffs',
        coach='Wayne Gretzky'
    )
    team13 = Team(
        year='2009-10',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='50-25-7',
        playoffs='Lost in round 1',
        coach='Dave Tippett'
    )
    team14 = Team(
        year='2010-11',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='43-26-13',
        playoffs='Lost in round 1',
        coach='Dave Tippett'
    )
    team15 = Team(
        year='2011-12',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='42-27-13',
        playoffs='Lost in conference finals',
        coach='Dave Tippett'
    )
    team16 = Team(
        year='2012-13',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='21-18-9',
        playoffs='Missed playoffs',
        coach='Dave Tippett'
    )
    team17 = Team(
        year='2013-14',
        team_name='Phoenix Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='37-30-15',
        playoffs='Missed playoffs',
        coach='Dave Tippett'
    )
    team18 = Team(
        year='2014-15',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='24-50-8',
        playoffs='Missed playoffs',
        coach='Dave Tippett'
    )
    team19 = Team(
        year='2015-16',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='35-39-8',
        playoffs='Missed playoffs',
        coach='Dave Tippett'
    )
    team20 = Team(
        year='2016-17',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='30-42-10',
        playoffs='Missed playoffs',
        coach='Dave Tippett'
    )
    team21 = Team(
        year='2017-18',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='29-41-12',
        playoffs='Missed playoffs',
        coach='Rick Tocchet'
    )
    team22 = Team(
        year='2018-19',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='39-35-8',
        playoffs='Missed playoffs',
        coach='Rick Tocchet'
    )
    team23 = Team(
        year='2019-20',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='33-29-8',
        playoffs='Lost in round',
        coach='Rick Tocchet'
    )
    team24 = Team(
        year='2020-21',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-03-21.png',
        record='24-26-6',
        playoffs='Missed playoffs',
        coach='Rick Tocchet'
    )
    team25 = Team(
        year='2021-22',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-21-24.png',
        record='25-50-7',
        playoffs='Missed playoffs',
        coach='Andre Tourigny'
    )
    team26 = Team(
        year='2022-23',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-21-24.png',
        record='28-40-14',
        playoffs='Missed playoffs',
        coach='Andre Tourigny'
    )
    team27 = Team(
        year='2023-24',
        team_name='Arizona Coyotes',
        logo='https://samsclub13.s3.us-west-2.amazonaws.com/logo-21-24.png',
        record='36-41-5',
        playoffs='Missed playoffs',
        coach='Andre Tourigny'
    )

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)
    db.session.add(team4)
    db.session.add(team5)
    db.session.add(team6)
    db.session.add(team7)
    db.session.add(team8)
    db.session.add(team9)
    db.session.add(team10)
    db.session.add(team11)
    db.session.add(team12)
    db.session.add(team13)
    db.session.add(team14)
    db.session.add(team15)
    db.session.add(team16)
    db.session.add(team17)
    db.session.add(team18)
    db.session.add(team19)
    db.session.add(team20)
    db.session.add(team21)
    db.session.add(team22)
    db.session.add(team23)
    db.session.add(team24)
    db.session.add(team25)
    db.session.add(team26)
    db.session.add(team27)

    db.session.commit()

def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
