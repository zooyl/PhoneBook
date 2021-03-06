from django.db import models

# Create your models here.

c_type = (
    (1, 'Mobile'),
    (2, 'Work'),
    (3, 'Home'),
    (4, 'Fax'),
    (5, 'Personal')
)

e_type = (
    (1, 'Work'),
    (2, 'Personal')
)


class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=128, blank=True)
    street = models.CharField(max_length=128, blank=True)
    house_nr = models.IntegerField(null=True, blank=True)
    flat_nr = models.IntegerField(null=True, blank=True)
    occupant_key = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='occupant_key')


class Phone(models.Model):
    number = models.IntegerField(unique=True)
    type = models.IntegerField(choices=c_type, default=1)
    phone_key = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='phone_key')


class Email(models.Model):
    email = models.EmailField(max_length=64, unique=True)
    email_type = models.IntegerField(choices=e_type, default=2)
    email_key = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='email_key')


class Group(models.Model):
    name = models.CharField(max_length=64, unique=True)
    group_key = models.ManyToManyField(Person)
