from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    mass = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    number_of_animals = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='animal_images/')

    def __str__(self):
        return f"{self.id} - {self.name}"

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.animal.name}"
