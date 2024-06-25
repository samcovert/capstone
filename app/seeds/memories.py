from app.models import db, Memory, environment, SCHEMA
from sqlalchemy.sql import text

def seed_memories():
    mem1 = Memory(
        title='I miss Jobing.com Arena',
        details='These were the glory days',
        user_id=1
    )

    db.session.add(mem1)
    db.session.commit()

def undo_memories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.memories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM memories"))

    db.session.commit()
