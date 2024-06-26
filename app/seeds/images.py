from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text

def seed_images():
    img1 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/jobing-arena.jpeg',
        memory_id=1
    )
    img2 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/doan-jersey.jpeg',
        merch_id=1
    )

    db.session.add(img1)
    db.session.add(img2)
    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
