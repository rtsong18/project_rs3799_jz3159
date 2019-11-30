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
                    longtitude=row[0]
                    latitude=row[1]
                )
