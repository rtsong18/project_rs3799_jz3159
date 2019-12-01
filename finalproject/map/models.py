from django.db import models

# Create your models here.
class map(models.Model):

    latitude  = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text = ('latitude'),
    )
    longtitude  = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text = ('longitude'),
    )
