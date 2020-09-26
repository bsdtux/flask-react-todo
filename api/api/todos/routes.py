from flask import Blueprint, jsonify, request
from flask.views import MethodView
from api import db
from api.todos.models import Todo, todo_schema, todos_schema


todo_bp = Blueprint('todo_api', __name__)

class TodosAPI(MethodView):

    def get(self, todo_id):
        if todo_id:
            todo = Todo.query.get(todo_id)
            data = todo_schema.dump(todo)
        else:
            todos = Todo.query.all()
            data = todos_schema.dump(todos)
        return jsonify({'success': True, 'errors': None, 'data': data})

    def post(self):
        data = request.json
        new_todo = Todo(title=data.get('title'), notes=data.get('notes'))
        db.session.add(new_todo)
        db.session.commit()

        data = todo_schema.dump(new_todo)
        return jsonify({'success': True, 'errors': None, 'data': data})

    def put(self, todo_id):
        todo = Todo.query.get(todo_id)
        data = request.json

        todo.title = data.get('title')
        todo.notes = data.get('notes') or ''

        db.session.commit()

        data = todo_schema.dump(data)

        return jsonify({'success': True, 'errors': None, 'data': data})

    def delete(self, todo_id):
        todo = Todo.query.get(todo_id)

        db.session.delete(todo)
        db.session.commit()
        return jsonify({'success': True, 'errors': None, 'data': None})


todo_view = TodosAPI.as_view('todo_api')
todo_bp.add_url_rule('/todos/', defaults={'todo_id': None},
                 view_func=todo_view, methods=['GET',])
todo_bp.add_url_rule('/todos/', view_func=todo_view, methods=['POST',])
todo_bp.add_url_rule('/todos/<int:todo_id>', view_func=todo_view,
                 methods=['GET', 'PUT', 'DELETE'])
