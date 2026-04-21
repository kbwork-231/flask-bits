from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()

class Account(db.Model):
    account_id = db.Column(db.String(12), primary_key=True, default=lambda: str(random.randint(100000000000, 999999999999)))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    account_type = db.Column(db.String(50), nullable=False, default='customer')

    def __repr__(self):
        return f'<Account {self.account_id}>'