from django.db import models

# Create your models here.
class squirrels(models.Model):
    latitude  = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text = ('latitude'),
    )
    longtitude  = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text = ('longitude'),
    )
    unique_squirrel_id = models.CharField(
        help_text = ('Unique Squirrel ID'),
        max_length = 200,
        default=None,
    )
    hectare = models.CharField(
        help_text = ('Hectare'),
        max_length = 16,
        default=None,
    )
    hectare_squirrel_number = models.IntegerField(
        help_text = ('Hectare squirrel number '),
        default=None,
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
        max_length = 16,
        default=AM,
    )



    date = models.DateField(
        help_text = ('Date'),
        default=None,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    Age_Choices = (
       (ADULT, 'Adult'),
       (JUVENILE,'Juvenile'),
    )
    age = models.CharField(
        help_text = ('age'),
        choices = Age_Choices,
        max_length = 16,
        default=ADULT,
    )
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    WHITE = 'White'
    HL_Color_Choices = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'black'),
        (WHITE,'White'),
    )
    Color_Choices = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'black'),
    )
    primary_fur_color = models.CharField(
        help_text = ('primary fur color'),
        choices = Color_Choices,
        max_length = 16,
        default=BLACK,
    )
    highlight_fur_color = models.CharField(
        help_text = ('primary fur color'),
        choices = HL_Color_Choices,
        max_length = 16,
        default=BLACK,
    )
    COM='Gray+'
    combination = models.CharField(
        help_text = ('combination'),
        max_length = 200,
        default=COM,
    )

    color_notes = models.CharField(
        help_text = ('Color notes'),
        max_length = 200,
        blank=True,
        null=True,
        default='',
    ) 
    GROUND_PLANE = 'Ground plane'
    ABOVE_GROUND = 'Above ground'
    Location_Choices = (
        (GROUND_PLANE,'Ground plane'),
        (ABOVE_GROUND,'Above ground')
    )
    location = models.CharField(
        help_text = ('location'),
        choices = Location_Choices,
        max_length = 16,
        default=GROUND_PLANE
    )
    above_ground_sighter_measurement = models.CharField(
        help_text = ('Above Ground Sighter Measurement'),
        max_length=9,
        default=False,
    )
    specific_location = models.CharField(
        help_text = ('specific location'),
        max_length = 100,
        default=None,
    )
    running = models.BooleanField(
        help_text = ('running'),
        default=False,
    )
    chasing = models.BooleanField(
        help_text = ('chasing'),
        default=False,
    )
    climbing  = models.BooleanField(
        help_text = ('climbing'),
        default=False,
    )
    eating = models.BooleanField(
        help_text = ('eating'),
        default=False,
    )
    foraging = models.BooleanField(
        help_text = ('foraging'),
        default=False,
    )
    other_activities = models.CharField(
        help_text = ('other activities'),
        max_length = 100,
        default=None,
    )
    kuks = models.BooleanField(
        help_text = ('kuks'),
        default=False,
    )
    quaas = models.BooleanField(
        help_text = ('quaas'),
        default=False,
    )
    moans = models.BooleanField(
        help_text = ('moans'),
        default=False,
    )
    tail_flags = models.BooleanField(
        help_text = ('tail flags'),
        default=False,
    )
    tail_twitches = models.BooleanField(
        help_text = ('tail twitches'),
        default=False,
    )
    approaches = models.BooleanField(
        help_text = ('approaches'),
        default=False,
    ) 
    indifferent = models.BooleanField(
        help_text = ('indifferent'),
        default=False,
    )
    runs_from = models.BooleanField(
        help_text = ('runs from'),
        default=False,
    )
    other_interactions = models.CharField(
        help_text = ('other interactions'),
        max_length = 100,
        default=None,
    )
    lati_long = models.CharField(
        help_text = ('lati_long'),
        max_length = 100,
        default=None,
   )
    zip_codes = models.CharField(
        help_text = ('zip codes'),
        max_length=100,
        default=None,
    )
    community_districts = models.CharField(
        help_text = ('Community Districts'),
        max_length=10,
        default=None,
    )
    borough_boundaries = models.CharField(
        help_text = ('Borough Boundaries'),
        max_length=10,
        default=None,
    )
    city_council_districts = models.CharField(
        help_text = ('City Council Districts'),
        max_length=10,
        default=None,
    )
    police_precincts = models.CharField(
        help_text = ('Police Precincts'),
        max_length=10,
        default=None,
    )

