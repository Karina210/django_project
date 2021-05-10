from django.db import models

# Create your models here.


class Customer(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'name: {self.firstname} | lastname: {self.lastname} | age: {self.age}'


class Group(models.Model):
    name = models.CharField(max_length=255)


class ContactInfo(models.Model):
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)


class Diary(models.Model):
    average_points = models.FloatField()

    student = models.OneToOneField('Student', null=True, related_name='diary', on_delete=models.SET_NULL)


class Project(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField()
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(blank=True, null=True)


class Book(models.Model):
    name = models.CharField(max_length=255)
    pages = models.IntegerField()


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()

    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, related_name='students', )
    contact_info = models.OneToOneField(ContactInfo, null=True, related_name='student', on_delete=models.SET_NULL)
    projects = models.ManyToManyField(Project, related_name='students')
    book = models.OneToOneField(Book, null=True, related_name='student', on_delete=models.SET_NULL)

    def __str__(self):
        return f'name: {self.firstname} | lastname: {self.lastname} | age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    count = models.IntegerField()
    comment = models.TextField()


class MusicBand(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    style = models.CharField(max_length=255)
    album = models.ManyToManyField('Album', related_name='album')


class Album(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    track = models.ManyToManyField('Track')

    def __str__(self):
        return f'{self.name}|{self.year}|{self.track}'


class Track(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()


