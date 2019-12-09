import csv
from  map.models import squirrels
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args,**options):
        with open(options['csv_file'], 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            i=0
            for row in reader:
                if i==0:
                    i=i+1
                    continue
                squirrels.objects.create(
                    longtitude=float(row[0]),
                    latitude=float(row[1]),
                    unique_squirrel_id=row[2],
                    hectare=row[3],
                    shift =row[4],
                    date=row[5][4::]+'-'+row[5][0:2]+'-'+row[5][2:4],
                    hectare_squirrel_number=row[6],
                    age=row[7],
                    primary_fur_color=row[8],
                    highlight_fur_color=row[9],
                    combination=row[10],
                    color_notes=row[11],
                    location=row[12],
                    above_ground_sighter_measurement=row[13],
                    specific_location=row[14],
                    running=bool(row[15]),
                    chasing=bool(row[16]),
                    climbing=bool(row[17]),
                    eating=bool(row[18]),
                    foraging=bool(row[19]),
                    other_activities=row[20],
                    kuks=bool(row[21]),
                    quaas=bool(row[22]),
                    moans=bool(row[23]),
                    tail_flags=bool(row[24]),
                    tail_twitches=bool(row[25]),
                    approaches=bool(row[26]),
                    indifferent=bool(row[27]),
                    runs_from=bool(row[28]),
                    other_interactions=row[29],
                    lati_long=row[30],
                    zip_codes=row[31],
                    community_districts=row[32],
                    borough_boundaries=row[33],
                    city_council_districts=row[34],
                    police_precincts=row[35],
                     )

