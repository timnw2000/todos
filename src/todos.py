import csv
from dataclasses import dataclass
import os
import sqlite3
import sys

from datetime import datetime

class ToDos:
    def __init__(self):
        database_connection = sqlite3.connect("database/data.db")
        self.connection = True if os.path.exists("data.db") else False
        self.weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        

    def __repr__(self):
        ...
    
    def __str__(self):
        ...

    def add(self, weekday, todo):
        cursor = self.database_connection.cursor()
        if not self.connection:
            sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
        fieldnames = ["id", "time", "category", "description", "importance"]
        match weekday.lower().strip():
            case "monday":
                self.monday.append(todo)
            case "tuesday":
                self.tuesday.append(todo)
            case "wednesday":
                self.wednesday.append(todo)
            case "thursday":
                self.thursday.append(todo)
            case "friday":
                self.friday.append(todo)
            case "saturday":
                self.saturday.append(todo)
            case "sunday":
                self.sunday.append(todo)
            case _:
                sys.exit("There is no such day in the week")

    def show(self, weekday=None):
        if not self.connection:
            sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
        if weekday is None:
            ...#print everyToDo of every day
        elif weekday not in self.weekdays:
            sys.exit("")
        

    def create_database(self):
        if not os.path.exists("data.db"):
            ...
            #some sql lite code to create the wanted database with the needed tables
            # Connect to the database
            #return connection object
        
        #connect to the database
        #return connection object

    


    def remove(self, weekday, id):
        if not self.connection:
            sys.exit("ToDo-list wasn't initialized use <todo init> to initialize the ToDo-list")
        match weekday.lower().strip():
            case "monday":
                for idx, todo in enumerate(self.monday):
                    if todo.id == id:
                        self.monday.pop(idx)
            case "tuesday":
                for idx, todo in enumerate(self.tuesday):
                    if todo.id == id:
                        self.tuesday.pop(idx)
            case "wednesday":
                for idx, todo in enumerate(self.wednesday):
                    if todo.id == id:
                        self.wednesday.pop(idx)
            case "thursday":
                for idx, todo in enumerate(self.thursday):
                    if todo.id == id:
                        self.thursday.pop(idx)
            case "friday":
                for idx, todo in enumerate(self.friday):
                    if todo.id == id:
                        self.friday.pop(idx)
            case "saturday":
                for idx, todo in enumerate(self.saturday):
                    if todo.id == id:
                        self.saturday.pop(idx)
            case "sunday":
                for idx, todo in enumerate(self.sunday):
                    if todo.id == id:
                        self.sunday.pop(idx)

    

@dataclass
class ToDo:
    time: str
    category: str
    description: str
    importance: str



if __name__ == "__main__":
    todos = ToDos()

    todo1 = ToDo("11:30", "test", "some description", "high")
    todo2 = ToDo("12:30", "someother test", "someother description", "high")

    todos.add("sunday", todo1)
    todos.add("wednesday", todo2)