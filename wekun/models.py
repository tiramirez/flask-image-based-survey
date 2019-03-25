from datetime import datetime
from wekun import db

class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, autoincrement=True)
    user_id = db.Column(db.String(50), primary_key=True, nullable=False) ## image id
    device_id = db.Column(db.String(50), nullable=True) ## image id
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Text, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    nationality = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    comuna = db.Column(db.String(50), nullable=True)
    ip_address = db.Column(db.String(50), nullable=True)
    education = db.Column(db.String(50), nullable=False)
    transport = db.Column(db.String(50), nullable=False)

    # state = db.Column(db.String(50))
    # answers = db.relationship('Answer', backref='author',lazy=True)

    def __repr__(self):
        return f'''User:('{self.id}','{self.user_id}','{self.device_id}','{self.gender}','{self.age}','{self.nationality}','{self.country}','{self.region}','{self.comuna}','{self.ip_address}','{self.education}','{self.transport}','{self.create_at}')'''


class Answers(db.Model):

    __tablename__ = 'Answers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(50), db.ForeignKey('Users.user_id'), nullable=False)
    img_1 = db.Column(db.String(50), nullable=True) ## image id
    img_2 = db.Column(db.String(50), nullable=True) ## image id
    choice = db.Column(db.String(20), nullable=True) ## image_1/image_2/equal/error
    question = db.Column(db.Integer, nullable=False)

############## Questions #############
#      1: Walkability
#      2: Better place to live
#      3: Boring
#      4: Beauty
#      5: Wealthy
##################################

    create_at = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Answer:('{self.id}','{self.user_id}','{self.question}','{self.img_1}','{self.img_2}','{self.choice}', '{self.create_at}')"