from django.db import models


class Review(models.Model):
    content = models.IntegerField()
    gamer_id = models.ForeignKey("Gamer", on_delete=models.CASCADE),
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)