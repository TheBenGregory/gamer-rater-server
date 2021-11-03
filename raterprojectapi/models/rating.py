from django.db import models
from django.db.models.fields import IntegerField


class Rating(models.Model):
    score = models.IntegerField()
    gamer_id = models.ForeignKey("Gamer", on_delete=models.CASCADE),
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)