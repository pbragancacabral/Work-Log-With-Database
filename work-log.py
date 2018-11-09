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
    minutes = IntegerField
    notes = TextField(default="")

    class Meta:
        database = db


def show_menu():
    choice = None
    while choice != "q":
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
    """Find a task by owner, date, time or search term."""
    clear()
    pass


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

if __name__ == "__main__":
    initialize()
