from manage import db, app

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, 
        primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
    
class Video(db.Model):
    __tablename__ = 'videos'
    
    id = db.Column(db.Integer,
        primary_key=True)
    video_url = db.Column(db.String(200), index=True, unique=True)
    
    def __repr__(self):
        return '<Video %r>' % (self.video_url)
    