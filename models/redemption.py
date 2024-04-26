from db import db

class Redemption(db.Model):
  __tablename__ = "redemptions"

  id = db.Column(db.Integer, primary_key=True)
  reward_id = db.Column(db.Integer, unique=False, nullable=False)
  user_id = db.Column(db.Integer, unique=False, nullable=False)