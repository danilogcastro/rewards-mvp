class PointsCalculator:
  def __init__(self, transactions):
    self.transactions = transactions

  @classmethod
  def execute(cls, transactions):
    earned = sum([transaction.points_earned if transaction.points_earned else 0 for transaction in transactions])
    spent = sum([transaction.points_spent if transaction.points_spent else 0 for transaction in transactions ])

    return earned - spent