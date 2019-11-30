from django.db import models

# Create your models here.
class map(models.Model):

    latitude  = models.DecimalField(
        help_text = ('latitude'),
    )
    longitude  = models.DecimalField(
        help_text = ('longitude'),
    )
