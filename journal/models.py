from django.db import models

choises = [
    ('5', 'пять'),
    ('4', 'четыре'),
    ('3', 'три'),
    ('2', 'два'),
    ('1', 'единица'),
]


class Class(models.Model):
    name = models.CharField(max_length=3, default='5Б')
    year = models.IntegerField()
    students = models.ManyToManyField("Student")


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    subjects = models.ManyToManyField("Subjects")
    marks = models.CharField(choices=choises, max_length=10)


class Subjects(models.Model):
    name = models.CharField(max_length=15)
