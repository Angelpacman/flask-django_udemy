from peewee import *
import datetime

db = SqliteDatabase('diary.db') #instancia de la base de datos

class Entry(Model):
    #fecha-timestamp
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def add_entry():
    """Registrar una entrada en nuestro diario"""

def view_entries():
    """despliaga nuestras entradas"""

def delete_entry():
    """borra un registro"""

def menu_loop():
    """muestra el menu con las opciones"""

def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)

if __name__ == '__main__':
    initialize()
    menu_loop()
