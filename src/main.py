import os
import sys

from todos import ToDos, ToDo


todos = ToDos()

def add_todo(todos):
    if len(sys.argv) != 3:
        sys.exit(f"Invalid Usage: {sys.argv[0]} monday/tuesday/etc.")
    todo = ToDo(sys.argv[1], sys.argv[2], input("Description: ").strip(), input("Importance: ").strip())
    todos.add(todo)

def init(todos):
    ToDos.create_database()

def remove_todo(todos)
    if len(sys.argv) != 3:
        sys.exit(f"Invalid Usage: {sys.argv[0]} monday/tuesday/etc.")

def show(todos):
    if len(sys.argv) == 2:
        todos.show()
    elif len(sys.argv) == 3:
        todos.show(sys.argv[2])
    
