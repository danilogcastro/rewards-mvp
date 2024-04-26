from marshmallow import Schema, fields

class TransactionSchema(Schema):
  id = fields.Int(dump_only=True)
  points_earned = fields.Int()
  points_spent = fields.Int()
  user_id = fields.Int(required=True)

class PointsSchema(Schema):
  user_id = fields.Int(required=True)
  total_points = fields.Int(dump_only=True)