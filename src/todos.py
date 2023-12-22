from dataclasses import dataclass
import sys
import csv

class ToDos:
    def __init__(self):
        self.monday = []
        self.tuesday = []
        self.wednesday = []
        self.thursday = []
        self.friday = []
        self.saturday = []
        self.sunday = []

    def __repr__(self):
        ...
    
    def __str__(self):
        ...

    def add(self, weekday, todo):
        
        match weekday.lower().strip():
            case "monday":
                self.monday.append(todo)
                with open("monday.csv") as monday:
                    writer = csv.DictWriter()
                    

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

    def show(self):
        ...

    def remove(self, weekday, id):
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
    id: int
    category: str
    description: str
    importance: str
