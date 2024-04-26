from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import *
from schemas import PointsSchema
from services.points_calculator import PointsCalculator

blp = Blueprint("Points", __name__)

@blp.post("/points")
@blp.arguments(PointsSchema)
@blp.response(201, PointsSchema)
def get(points_data):
  user_id = points_data['user_id']
  transactions = Transaction.query.filter_by(user_id=user_id).all()
  
  try:
    total_points = PointsCalculator.execute(transactions)
  except SQLAlchemyError:
    abort(500, message="Ocorreu um erro")

  return { "total_points": total_points }
