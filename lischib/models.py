from lischib import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_confirmed = db.Column(db.Boolean, default=False)
    