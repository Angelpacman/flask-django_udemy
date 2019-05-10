from peewee import *

db = SqliteDatabase('diary.db') #instancia de la base de datos

class Entry(Model):
    #fecha-timestamp

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

if __name__ == '__main__':
    menu_loop()
