#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import os

from peewee import *

db = SqliteDatabase("database.db")


class Task(Model):
    owner = CharField(max_length=255)
    date = DateTimeField(default=datetime.datetime.now)
    title = CharField(max_length=255)
    minutes = IntegerField()
    notes = TextField(default="")

    class Meta:
        database = db

    def __repr__(self):
        print(self.owner)
        print(self.date)
        print(self.title)
        print(self.minutes)
        print(self.notes)


def show_menu():
    choice = None
    while choice != "q":
        clear()
        print("Press 'Q' to quit.")
        for key, value in menu.items():
            print(f"{key}) {value.__doc__}")
        choice = input("Please select an option: ").lower().strip()

        if choice in menu:
            menu[choice]()
    print("Thank you.")


def add_task():
    """Add a task to the database."""
    clear()
    task = dict()
    task["owner"] = input("What's your name? ")
    task["title"] = input("What's the task title? ")
    task["minutes"] = input("How many minutes it takes? ")
    task["notes"] = input("Additional notes: (optional) ")

    if input("Save data? [yn] ").lower() == "y":
        Task.create(**task)
        print("Task created and saved successfully!")


def find_task():
    """Find a task."""
    clear()
    for key, value in find_task_menu.items():
        print(f"{key}) {value.__doc__}")

    choice = input("Please select an option: ").lower().strip()
    if choice in find_task_menu:
        find_task_menu[choice]()


def find_by_owner():
    """Find a task by owner."""
    clear()
    search_query = input("Name of the owner: ")
    tasks = Task.select().order_by(Task.owner)
    tasks = tasks.where(Task.owner.contains(search_query))
    for task in tasks:
        print(task)


def find_by_date():
    """Find a task by date."""
    clear()


def find_by_time():
    """Find a task by time."""
    clear()
    search_query = input("What is the time spent in minutes? ")
    tasks = Task.select().where(Task.minutes == search_query)
    for task in tasks:
        print(task)


def find_by_search_term():
    """Find a task by search term."""
    clear()
    search_query = input("Type a search query term: ")
    tasks = Task.select().where(
        Task.title.contains(search_query) |
        Task.notes.contains(search_query)
    )
    for task in tasks:
        print(task.__repr__())


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def initialize():
    db.connect()
    db.create_tables([Task], safe=True)
    show_menu()


menu = OrderedDict([
    ("a", add_task),
    ("f", find_task),
])

find_task_menu = OrderedDict([
    ("o", find_by_owner),
    ("d", find_by_date),
    ("t", find_by_time),
    ("s", find_by_search_term),
])

if __name__ == "__main__":
    initialize()
