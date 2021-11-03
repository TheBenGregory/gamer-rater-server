from django.db import models



class GameCategory(models.Model):

    categories_id = models.ForeignKey("Category", on_delete=models.CASCADE),
    games_id = models.ForeignKey("Game", on_delete=models.CASCADE)
