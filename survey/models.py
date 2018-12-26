from datetime import datetime
from survey import db ## from survey import db

class User(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Text, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    country = db.Column(db.String(50), nullable=False)
    # state = db.Column(db.String(50))
    # answers = db.relationship('Answer', backref='author',lazy=True)

    def __repr__(self):
        return f"User:('{self.id}','{self.gender}','{self.age}','{self.country}','{self.create_at}')"


class Answer(db.Model):

    __tablename__ = 'Answers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    img_1 = db.Column(db.String(50), nullable=True)
    img_2 = db.Column(db.String(50), nullable=True)
    choice = db.Column(db.String(20), nullable=True)
    question = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Answer:('{self.id}','{self.user_id}','{self.img_1}','{self.img_2}','{self.choice}', '{self.create_at}')"

class Images(db.Model):

    __tablename__ = 'Images'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img_id = db.Column(db.String(50), nullable=True)
    category = db.Column(db.String(20), nullable=True)
    create_at = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Answer:('{self.id}','{self.img_id}','{self.category}','{self.create_at}')"