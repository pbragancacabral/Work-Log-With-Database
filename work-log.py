#!/usr/bin/env python3
import datetime

from peewee import *

db = SqliteDatabase("database.db")


class Task(Model):
    owner = CharField(max_length=255)
    date = DateTimeField(default=datetime.datetime.now)
    title = CharField(max_length=255)
    minutes = IntegerField
    notes = TextField()

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Task], safe=True)


if __name__ == "__main__":
    initialize()