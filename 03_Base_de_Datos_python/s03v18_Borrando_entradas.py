from peewee import *
from collections import OrderedDict
import datetime
import sys
db = SqliteDatabase('diary.db') #instancia de la base de datos

class Entry(Model):
    #fecha-timestamp
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def add_entry():
    """Registrar una entrada en nuestro diario"""
    print("\nIntroduce tu registro, presiona Ctrl + D cuando termines")
    data = sys.stdin.read().strip()
    if data:
        if input('Guardar entrada?? [Yn]').lower() != 'n':
            Entry.create(content = data)
            print('Guardada exitosamente')

def view_entries(search_query=None):
    """ver nuestros registros"""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print(entry.content)
        print('\nn| siguiente entrada')
        print('d| Borrar entrada')
        print('q| salir al menu')


        next_action = input('Accion a realizar: [Nq]').lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Busca una entrada con cierto texto"""
    view_entries(input('Texto a buscar: '))


def delete_entry(entry):
    """borra un registro"""
    response = input("Estas seguro? [yN]").lower()
    if response == 'y':
        entry.delete_instance()
        print('Entrada borrada')

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])

def menu_loop():
    """muestra el menu con las opciones"""
    choice = None
    while choice != 'q':
        print("Presiona 'q' para salir \n")
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
