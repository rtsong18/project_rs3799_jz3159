from django.db import models

# Create your models here.
class sightings(models.Model):

    latitude  = models.DecimalField(
            max_digits=5, decimal_places=2,
            help_text = ('latitude'),
    )
    longitude  = models.DecimalField(
            max_digits=5, decimal_places=2,
            help_text = ('longitude'),
    )
    Unique_Squirrel_ID = models.IntegerField(
        help_text = ('Unique Squirrel_ID'),
    )



    AM = 'AM'
    PM = 'PM'
    Shift_Choices = (
        (AM,'AM'),
        (PM,'PM'),
    )
    shift = models.CharField(
        help_text = ('shift'),
        choices = Shift_Choices,
        max_length = 16
    )



   ###need to be in the setting.py  DATE_INPUT_FORMATS = ['%m%d%y']
    Date = models.DateField(
        help_text = ('Date'),
    )



    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    Age_Choices = (
        (ADULT, 'Adule'),
        (JUVENILE,'Juvenile'),
    )
    age = models.CharField(
        help_text = ('age'),
        choices = Age_Choices,
        max_length = 16
    )


    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    WHITE = 'White'
    Color_Choices = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'black'),
        (WHITE,'White'),
    )
    primary_fur_color = models.CharField(
        help_text = ('primary fur color'),
        choices = Color_Choices,
        max_length = 16,
    )


    GROUND_PLANE = 'Ground plane'
    ABOVE_GROUND = 'Above ground'
    Location_Choices = (
        (GROUND_PLANE,'Ground plane'),
        (ABOVE_GROUND,'Above ground'),
    )
    location = models.CharField(
        help_text = ('location'),
        choices = Location_Choices,
        max_length = 16,
    )


    specific_location = models.CharField(
        help_text = ('specific location'),
        max_length = 100,
    )


    running = models.BooleanField(
        help_text = ('running'),
    )
    chasing = models.BooleanField(
        help_text = ('chasing'),
    )
    climbing  = models.BooleanField(
        help_text = ('climbing'),
    )
    eating = models.BooleanField(
        help_text = ('eating'),
    )
    foraging = models.BooleanField(
        help_text = ('foraging'),
    )

    other_activities = models.CharField(
        help_text = ('other activities'),
        max_length = 100,
    )

    kuks = models.BooleanField(
        help_text = ('kuks'),
    )
    quaas = models.BooleanField(
        help_text = ('quaas'),
    )
    moans = models.BooleanField(
        help_text = ('moans'),
    )
    tail_flags = models.BooleanField(
        help_text = ('tail flags'),
    )
    tail_twitches = models.BooleanField(
        help_text = ('tail twitches'),
    )
    approaches = models.BooleanField(
        help_text = ('approaches'),
    )
    indifferent = models.BooleanField(
        help_text = ('indifferent'),
    )
    runs_from = models.BooleanField(
        help_text = ('runs from'),
         )
