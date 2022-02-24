from . import db
from flask_login import UserMixin
import datetime

class FeedbackModel(db.Model, UserMixin):
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer, default=False, nullable=False)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    creation_date = db.Column(db.String(255), nullable=True, default=datetime.datetime.now())

    def __init__(self, rate, title, description):
        self.rate = rate
        self.title = title
        self.description = description


    def range_rate(self, number):
        return "Ola"