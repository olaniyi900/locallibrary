from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name