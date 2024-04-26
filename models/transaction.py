from db import db

class Transaction(db.Model):
  __tablename__ = "transactions"

  id = db.Column(db.Integer, primary_key=True)
  points_earned = db.Column(db.Integer, unique=False, nullable=True)
  points_spent = db.Column(db.Integer, unique=False, nullable=True)
  user_id = db.Column(db.Integer, unique=False, nullable=False)