from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import *
from schemas import TransactionSchema

blp = Blueprint("Transactions", __name__)

@blp.post("/transactions")
@blp.arguments(TransactionSchema)
@blp.response(201, TransactionSchema)
def create(transaction_data):
  transaction = Transaction(**transaction_data)

  try:
    db.session.add(transaction)
    db.session.commit()
  except SQLAlchemyError:
    abort(500, message="Ocorreu um erro")

  return transaction
