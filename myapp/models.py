from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    years_of_experience = models.IntegerField(default=0)
    subject = models.CharField(max_length=255, default='Mathematics')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




