from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text

def seed_images():
    img1 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/jobing-2.jpeg',
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
    img10 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/jobing-arena.jpeg',
        memory_id=1
    )
    img11 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/2012-pic.jpeg',
        memory_id=2
    )
    img12 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/2012-2.jpeg',
        memory_id=2
    )
    img13 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/2102-3.jpeg',
        memory_id=2
    )
    img14 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/whiteout.jpeg',
        memory_id=3
    )
    img15 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/whiteout-2.jpeg',
        memory_id=3
    )
    img16 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/smith-goal-3.jpeg',
        memory_id=4
    )
    img17 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/smith-goal-2.jpeg',
        memory_id=4
    )
    img18 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/smith-goal.jpeg',
        memory_id=4
    )
    img19 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/josh-doan.jpeg',
        memory_id=5
    )
    img20 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/josh-doan-2.jpeg',
        memory_id=5
    )
    img21 = Image(
        url='https://samsclub13.s3.us-west-2.amazonaws.com/josh-doan-3.jpeg',
        memory_id=5
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
    db.session.add(img10)
    db.session.add(img11)
    db.session.add(img12)
    db.session.add(img13)
    db.session.add(img14)
    db.session.add(img15)
    db.session.add(img16)
    db.session.add(img17)
    db.session.add(img18)
    db.session.add(img19)
    db.session.add(img20)
    db.session.add(img21)

    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
