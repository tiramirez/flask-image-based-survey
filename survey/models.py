from datetime import datetime
from wekun import db

class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, autoincrement=True)
    user_id = db.Column(db.String(50), primary_key=True, nullable=False) ## image id
    device_id = db.Column(db.String(50), nullable=True) ## image id
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    nationality = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    comuna = db.Column(db.String(50), nullable=True)
    ip_address = db.Column(db.String(50), nullable=False)
    education = db.Column(db.String(50), nullable=False)
    transport = db.Column(db.String(50), nullable=False)
    browser = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    psico1 = db.Column(db.String(50), nullable=True)
    psico2 = db.Column(db.String(50), nullable=True)
    psico3 = db.Column(db.String(50), nullable=True)
    psico4 = db.Column(db.String(50), nullable=True)
    psico5 = db.Column(db.String(50), nullable=True)
    psico6 = db.Column(db.String(50), nullable=True)
    psico7 = db.Column(db.String(50), nullable=True)
    psico8 = db.Column(db.String(50), nullable=True)
    psico9 = db.Column(db.String(50), nullable=True)
    psico10 = db.Column(db.String(50), nullable=True)
    income = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"User:('{self.id}','{self.user_id}','{self.device_id}','{self.gender}','{self.age}','{self.nationality}','{self.country}','{self.region}','{self.comuna}','{self.ip_address}','{self.education}','{self.transport}','{self.browser}','{self.platform}','{self.create_at}','{self.psico1}','{self.psico2}','{self.psico3}','{self.psico4}','{self.psico5}','{self.psico6}','{self.psico7}','{self.psico8}','{self.psico9}','{self.psico10}','{self.income}"


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