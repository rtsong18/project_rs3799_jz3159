import csv
from  map.models import map
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                try:
                    map.objects.create(
                            longtitude=float(row[0]),
                            latitude=float(row[1]))
                except:
                    continue
