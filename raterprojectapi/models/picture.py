from django.db import models


class Picture(models.Model):
    image_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    gamer_id = models.ForeignKey("Gamer", on_delete=models.CASCADE),
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)