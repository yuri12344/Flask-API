from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime

class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(25), nullable=True, unique=True)
    password = db.Column(db.String(255), nullable=False)
    whatsapp = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(50), nullable=True)
    is_company = db.Column(db.Boolean, default=False, nullable=False)
    schedule = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    creation_date = db.Column(db.String(255), nullable=True, default=datetime.datetime.now())

    def __init__(self, name, mail, password, whatsapp, state, city, address, is_company, schedule, description):
        self.name = name
        self.mail = mail
        self.password = generate_password_hash(password)
        self.whatsapp = whatsapp
        self.state = state
        self.city = city
        self.address = address
        self.is_company = is_company
        self.schedule = schedule
        self.description = description

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)