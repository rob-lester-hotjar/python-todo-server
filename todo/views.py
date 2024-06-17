from dataclasses import asdict
from datetime import datetime
from flask import Blueprint

from .models import Todo


todos: list[Todo] = [
  {
    'id': 1,
    'title': 'Do the shopping',
    'description': 'Apples, pears, laundry detergent',
    'priority': 2,
    'updated_at': datetime.now(),
  },
  {
    'id': 2,
    'title': 'Send mail',
    'description': 'Urgent',
    'priority': 3,
    'updated_at': datetime.now(),
  },
  {
    'id': 3,
    'title': 'Read the news',
    'description': 'Smashing magazine, sidebar.io, Hacker News',
    'priority': 1,
    'updated_at': datetime.now(),
  },
]


bp = Blueprint('todos', __name__, url_prefix='/api/todos')


@bp.get('/')
def find_all() -> list[Todo]:
    """Get Todos listing"""
    return todos


@bp.get('/<int:todo_id>')
def find_by_id(todo_id: int) -> Todo:
    """Get a Todo by identifier"""
    raise NotImplementedError


@bp.post('/')
def add_todo() -> Todo:
    """Create a Todo"""
    raise NotImplementedError


@bp.put('/<int:todo_id>')
def update_todo(todo_id: int) -> Todo:
    """Update a Todo by its identifier"""
    raise NotImplementedError


@bp.delete('/<int:todo_id>')
def delete_todo(todo_id: int) -> Todo:
    """Delete a Todo by its identifier"""
    raise NotImplementedError
