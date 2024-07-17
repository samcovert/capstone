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
    img3 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/doan-jersery-front.jpeg',
        merch_id=1
    )
    img4 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/yotes-banner.jpeg',
        merch_id=2
    )
    img5 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/signed-pic.jpeg',
        merch_id=3
    )
    img6 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/whiteout-shirt.jpeg',
        merch_id=4
    )
    img7 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/stick.jpeg',
        merch_id=5
    )
    img8 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/stick2.jpeg',
        merch_id=5
    )
    img9 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/signed-jersey.jpeg',
        merch_id=6
    )

    db.session.add(img1)
    db.session.add(img2)
    db.session.add(img3)
    db.session.add(img4)
    db.session.add(img5)
    db.session.add(img6)
    db.session.add(img7)
    db.session.add(img8)
    db.session.add(img9)

    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
