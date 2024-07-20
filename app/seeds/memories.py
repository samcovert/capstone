from app.models import db, Memory, environment, SCHEMA
from sqlalchemy.sql import text

def seed_memories():
    mem1 = Memory(
        title='I miss Jobing.com Arena',
        details='These were the glory days',
        user_id=1
    )
    mem2 = Memory(
        title='Most memorable year?',
        details='2012 will be the popular answer, but I think 2013-14 was an underrated year. If Doaner didn\'t get hurt they would\'ve made the playoffs',
        user_id=3
    )
    mem3 = Memory(
        title='First Whiteout Game',
        details='You just had to be there',
        user_id=2
    )
    mem4 = Memory(
        title='Mike Smith Goal',
        details='This game was crazy and of course smitty scored to put away the wings',
        user_id=1
    )
    mem5 = Memory(
        title='Josh Doan first game',
        details='Salt Lake doesn\'t deserve the Doan Family!!',
        user_id=3
    )

    db.session.add(mem1)
    db.session.add(mem2)
    db.session.add(mem3)
    db.session.add(mem4)
    db.session.add(mem5)

    db.session.commit()

def undo_memories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.memories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM memories"))

    db.session.commit()
