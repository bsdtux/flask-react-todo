from datetime import datetime
from api import db, ma


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    notes = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title, notes):
        self.title = title
        self.notes = notes


# Marshmallow Schemas
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'notes', 'created_at')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
