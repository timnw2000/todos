import os

from todos import ToDos, ToDo


todos = todos.ToDos()

def add_todo(todos):
    if len(sys.argv) != 3:
        sys.exit(f"Invalid Usage: {sys.argv[0]} monday/tuesday/etc.")
    time = input("What time? (hh:mm)").strip()
    todo = ToDo()
    todos.add(sys.argv[2], todo)

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
    
