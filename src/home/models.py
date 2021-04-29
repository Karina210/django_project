from django.db import models

# Create your models here.
class Customer(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'name: {self.firstname} | lastname: {self.lastname} | age: {self.age}'


class Tickets(models.Model):

    name = models.CharField()
    first_country = models.CharField()
    last_country = models.CharField()
    people = models.CharField()
    data = models.CharField()

