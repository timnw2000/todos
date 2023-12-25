import os
import sys


from todos import ToDos, ToDo


def add_todo():
    todos = ToDos()
    if sys.argv[3] not in todos.weekdays:
        sys.exit("Not a valid day")
    try:
        todo = ToDo(sys.argv[2], sys.argv[3], input("Description: ").strip(), input("Importance: ").strip())
    except IndexError:
        sys.exit("Missing commeand line arguments => todo add <todo-name> <weekday>")
    else:
        todos.add(todo)

def init():
    ToDos.create_database()

def remove_todo():
    todos = ToDos()
    todos.remove()

def show():
    todos = ToDos()
    todos.show()

def show_history():
    todos = ToDos()
    todos.show_history()

def todo():
    if sys.argv[1] == "add":
        add_todo()
    elif sys.argv[1] == "init":
        init()
    elif sys.argv[1] == "remove":
        remove_todo()
    elif sys.argv[1] == "show":
        show()
    elif sys.argv[1] == "history":
        show_history()
    else:
        sys.exit("Invalid command")
