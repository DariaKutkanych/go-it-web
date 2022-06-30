from lib2to3.pgen2.token import NUMBER
from random import randint
from secrets import choice
import sqlite3
import faker


NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 3
NUMBER_STUDENTS = 30

def generate_fake_data(number_groups, number_subjects, number_teachers, number_students):

    fake_groups = [1, 2, 3]
    fake_subjects = ["Mathematics", "English", "Chemistry", "Biology", "Physics"]
    fake_teachers = []
    fake_students = []

    fake_data = faker.Faker()

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_students):
        fake_students.append(fake_data.name())
    
    return fake_groups, fake_teachers, fake_students, fake_subjects


def prepare_data(groups, teachers, students, subjects):

    for_groups = []
    for_teachers = []
    for_subjects = []
    for_student = []
    for_marks = []

    for group in groups:
        for_groups.append((group, ))
    
    for teacher in teachers:
        for_teachers.append((teacher, ))
        
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS, )))
    
    for student in students:
        for_student.append((student, randint(1, NUMBER_GROUPS, )))
    
    for st in range(NUMBER_STUDENTS):
        for _ in range(20):
            for_marks.append((randint(0,100), st + 1, randint(1, NUMBER_SUBJECTS, )))
    

    return for_groups, for_teachers, for_student, for_subjects, for_marks

def insert_data_to_db(groups, teachers, students, subjects, marks):

    with sqlite3.connect("education.db") as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(number) VALUES (?)"""
        sql_to_teachers = """INSERT INTO teachers(name) VALUES (?)"""
        sql_to_subjects = """INSERT INTO subjects(name, teacher_id) VALUES (?, ?)"""
        sql_to_students = """INSERT INTO students(name, group_id) VALUES (?, ?)"""
        sql_to_marks = """INSERT INTO marks(mark, student_id, subject_id) VALUES (?, ?, ?)"""

        cur.executemany(sql_to_groups, groups)
        cur.executemany(sql_to_teachers, teachers)
        cur.executemany(sql_to_subjects, subjects)
        cur.executemany(sql_to_students, students)
        cur.executemany(sql_to_marks, marks)

        con.commit()

if __name__=="__main__":

    groups, teachers, students, subjects = generate_fake_data(NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_TEACHERS, NUMBER_STUDENTS)
    groups, teachers, students, subjects, marks = prepare_data(groups, teachers, students, subjects)
    insert_data_to_db(groups, teachers, students, subjects, marks)
