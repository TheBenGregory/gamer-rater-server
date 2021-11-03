from django.db import models



class Game(models.Model):

    title = models.CharField(max_length=70),
    description = models.CharField(max_length=50),
    year_released = models.IntegerField(),
    number_of_players = models.IntegerField(),
    time_to_play = models.IntegerField(),
    age_rec = models.IntegerField(),
    designer = models.CharField(max_length=50),
    age_rec = models.IntegerField()