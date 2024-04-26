from marshmallow import Schema, fields, validates_schema, ValidationError

class TransactionSchema(Schema):
  id = fields.Int(dump_only=True)
  points_earned = fields.Int()
  points_spent = fields.Int()
  user_id = fields.Int(required=True)

  @validates_schema
  def validate_points_presence(self, data, **kwargs):
    points_earned_present = data.get('points_earned') is not None
    points_spent_present = data.get('points_spent') is not None

    if not (points_earned_present or points_spent_present):
      raise ValidationError("É necessário ter pontos ganhos ou pontos gastos")