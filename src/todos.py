import csv
from dataclasses import dataclass
import os
import sqlite3
import sys

import datetime

class ToDos:
    def __init__(self):
        self.database_connection = sqlite3.connect("data.db") if os.path.exists("data.db") else sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
        self.cursor = self.database_connection.cursor()
        self.initialized = True if os.path.exists("data.db") else False
        self.weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]





    def add(self, todo):
        if not self.initialized:
            sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
        if len(sys.argv) != 3:
            sys.exit("Wrong amount of command line arguments")
        data = (todo.todo, todo.weekday, todo.importance, todo.description)
        self.cursor.execute(
            "INSERT INTO todos (todo, weekday, importance, description) VALUES (?, ?, ?, ?)", data
        )
        self.database_connection.commit()
        
        



    def show(self):
        if not self.initialized:
            sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
        try:
            requested_weekday = sys.argv[1].lower().strip()
        except IndexError:
            todos_for_the_day = self.cursor.execute("SELECT * FROM todos")
            for todo in todos_for_the_day:
                print(todo)
        else:
            if requested_weekday in self.weekdays:
                todos_for_the_day = self.cursor.execute("SELECT * FROM todos WHERE weekday = ?", (requested_weekday,))
                for todo in todos_for_the_day:
                    print(todo)

        



        
    @classmethod
    def create_database(cls):
        if not os.path.exists("data.db"):
            try:
                conn = sqlite3.connect("data.db")
                cur = conn.cursor()
                cur.execute("""
                    CREATE TABLE todos (
                        id INTEGER NOT NULL,
                        todo TEXT NOT NULL,
                        weekday TEXT NOT NULL,
                        time TEXT,
                        importance TEXT,
                        description TEXT,
                        PRIMARY KEY (id)
                        UNIQUE (todo)
                    )
                """)
                cur.execute("""
                    CREATE TABLE history (
                        id INTEGER NOT NULL,
                        todo TEXT NOT NULL,
                        scheduled TEXT NOT NULL,
                        finished_weekday TEXT NOT NULL,
                        finished_time TEXT,
                        description TEXT,
                        state TEXT NOT NULL
                    )
                """)
                conn.commit()
            except:
                sys.exit("Something went wrong")
            else:
                sys.exit("Successfully initialized")
       




    def remove(self):
        if not self.initialized:
            sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
    
        if len(sys.argv) == 2 and isinstance(int(sys.argv[1]), int):
            todos_for_history = self.cursor.execute("SELECT * FROM todos WHERE id = ?", (sys.argv[1],)).fetchone()
            id, todo, weekday,importance, description = todos_for_history
            finished = datetime.datetime.now().strftime("%B")
            data = (id, todo, weekday, finished, importance, description)
            self.cursor.execute(
                "INSERT INTO history (id, todo, scheduled, finished_weekday, importance, description) VALUES (?, ?, ?, ?, ?, ?)", data
            )
            
            
            self.cursor.execute(
                "DELETE FROM todos WHERE id = ?", sys.argv[1]
            )
            self.database_connection.commit()



    

@dataclass
class ToDo:
    todo: str
    weekday: str
    description: str
    importance: str



if __name__ == "__main__":
    ToDos.create_database()
    todos = ToDos()

    #if not len(sys.argv) == 4:
        #sys.exit("Invalid Usage: todo add <todo_name> <weekday>")
    #if sys.argv[3] not in todos.weekdays:
        #sys.exit("Invalid weekday")
    #todo = ToDo(sys.argv[1], sys.argv[2].lower(), input("Description: ").strip(), input("Importance: ").strip())
    #todos.add(todo)
    todos.remove()
    

    

