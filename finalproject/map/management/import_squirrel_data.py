import csv
from django.core.management import BaseCommand
from app.models import Question

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                question = Question.objects.create(
                    latitude =row[0]
                    longitude=row[1]
                    Unique_Squirrel_ID =row[2]
                    shift =row[3]
                    date=row[4]
                    age=row[5]
                    primary_fur_color=row[6]
                    highlight_Fur_color=row[7]
                    combination_of_primary_and_highlight_color==row[8]
                    color_notes==row[9]
                    location=row[10]
                    above_ground_sighter_measurement==row[11]
                    specific_location==row[12]
                    running==row[13]
                    chasing==row[14]
                    climbing==row[15]
                    eating==row[16]
                    foraging==row[17]
                    other_activities==row[18]
                    kuks==row[19]
                    quaas==row[20]
                    moans==row[21]
                    tail_flags==row[22]
                    tail_twitches==row[23]
                    approaches=row[24]
                    indifferent==row[25]
                    runs_from==row[26]
                    other_interactions==row[27]
                    lat/long_==row[28]
                    zip_codes==row[29]
                    community_districts==row[30]
                    borough_boundaries==row[31]
                    city_council_districts==row[32]
                    police_precincts==row[33]       
                )

