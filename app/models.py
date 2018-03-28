from app import db

class data(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    cloud = db.Column(db.String(12), index=True)
    jsond = db.Column(db.JSON(1000), index=True)

    def __repr__(self):
        return '<User %r>' % (self.sn)

