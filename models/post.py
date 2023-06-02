from app import app, db

class Post(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )
    header = db.Column(
        db.String(100),
        nullable=False, 
    )  
    body = db.Column(
        db.Text(),
        nullable=False, 
    )  
    user_ref = db.Column(
        db.String(180),
        db.ForeignKey("user.login"),
    )