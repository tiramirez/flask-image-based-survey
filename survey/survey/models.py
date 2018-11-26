from datetime import datetime
from survey import db ## from survey import db

class User(db.Model):
    """
    BucketItem model class
    """

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Text, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    country = db.Column(db.String(50), nullable=False)
    # state = db.Column(db.String(50))
    # answers = db.relationship('Answer', backref='author',lazy=True)

    def __init__(self, gender, age, country):
        self.gender = gender
        self.age = age
        self.country = country
        # self.state = state

    def __repr__(self):
        return f"User:('{self.id}','{self.age}')"

    # def save(self):
    #     """
    #     Persist Item into the database
    #     :return:
    #     """
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self, name, description=None):
    #     """
    #     Update the records in the item
    #     :param name: Name
    #     :param description: Description
    #     :return:
    #     """
    #     self.name = name
    #     if description is not None:
    #         self.description = description
    #     db.session.commit()

    # def delete(self):
    #     """
    #     Delete an item
    #     :return:
    #     """
    #     db.session.delete(self)
    #     db.session.commit()

    # def json(self):
    #     """
    #     Json representation of the model
    #     :return:
    #     """
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'description': self.description,
    #         'bucketId': self.bucket_id,
    #         'createdAt': self.create_at.isoformat(),
    #         'modifiedAt': self.modified_at.isoformat()
    #     }


class Answer(db.Model):
    """
    BucketItem model class
    """

    __tablename__ = 'Answers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    img_1 = db.Column(db.String(10), nullable=True)
    img_2 = db.Column(db.String(10), nullable=True)
    choice = db.Column(db.String(1), nullable=True)
    create_at = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)

    def __init__(self, user_id, img_1, img_2, choice):
        self.user_id = user_id
        self.img_1 = img_1
        self.img_2 = img_2
        self.choice = choice

    def __repr__(self):
        return f"Answer:('{self.id}','{self.user_id}','{self.img_1}','{self.img_2}','{self.choice}')"

    # def save(self):
    #     """
    #     Persist Item into the database
    #     :return:
    #     """
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self, name, description=None):
    #     """
    #     Update the records in the item
    #     :param name: Name
    #     :param description: Description
    #     :return:
    #     """
    #     self.name = name
    #     if description is not None:
    #         self.description = description
    #     db.session.commit()

    # def delete(self):
    #     """
    #     Delete an item
    #     :return:
    #     """
    #     db.session.delete(self)
    #     db.session.commit()