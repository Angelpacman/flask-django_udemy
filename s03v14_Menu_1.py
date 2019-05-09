from peewee import *
from collections import OrderedDict
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
    """ver nuestros registros"""

def delete_entry():
    """borra un registro"""

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    
])

def menu_loop():
    """muestra el menu con las opciones"""
    choice = None
    while choice != 'q':
        print("Presiona 'q' para salir")
        for key, value in menu.items():
            print('{}|{}'.format(key, value.__doc__) )
        choice = input('Election: ').lower().strip()

        if choice in menu:
            menu[choice]()

def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)

if __name__ == '__main__':
    initialize()
    menu_loop()
