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
    'points':3},
    {'username': 'pedro',
    'points':6},
    {'username': 'panchito',
    'points':7},
    {'username': 'tugfa',
    'points':7},
    {'username': 'pita',
    'points':5}
]

#esta funcion se hizo para poder sobre escribir la base de datos en cada uno de sus elementos
# sin que no s de un error al volver a correr el archivo python, ya que se anula aquel conflicto
# con el argunmeto unique=True en la linea 7
def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
            points = student['points'])
        except IntegrityError:
            student_record = Student.get(username = student['username'])
            student_record.points = student['points']
            student_record.save()


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe = True)

    add_students()
