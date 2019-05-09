from peewee import *

db = SqliteDatabase('students.db')
#db = SqlDatabase('students.db')

class Student(Model):
    username = CharField(max_length = 255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

students = [
    {'username': 'aldo',
    'points':10},
    {'username': 'pedro',
    'points':6},
    {'username': 'panchito',
    'points':7},
    {'username': 'tugfa',
    'points':7},
    {'username': 'pita',
    'points':5}
]

def add_students():
    for student in students:
        Student.create(username = student['username'],
        points = student['points'])



if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe = True)

    add_students()
