import csv
from map.models import squirrels
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')


    def handle(self, *app_labels, **options):

        with open(options['csv_file'],'w') as csvfile:
            writer = csv.writer(csvfile,dialect='excel')
            writer.writerow(['X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement', 'Specific Location','Running','Chasing','Climbing',      'Eating','Foraging','Other Activities', 'Kuks', 'Quaas', 'Moans','Tail flags','Tail twitches','Approaches', 'Indifferent','Runs from','Other Interactions', 'Lat/Long', 'Zip Codes','Community Districts','Borough Boundaries', 'City Council Districts','Police Precincts'])
            for obj in squirrels.objects.all()[0:]:
                writer.writerow([obj.longtitude,obj.latitude,obj.unique_squirrel_id,obj.hectare,obj.shift,obj.date,obj.hectare_squirrel_number,obj.age,obj.primary_fur_color,obj.highlight_fur_color,obj.combination,obj.color_notes,obj.location,obj.above_ground_sighter_measurement,obj.specific_location,obj.running,obj.chasing,obj.climbing,obj.eating,obj.foraging, obj.other_activities,obj.kuks, obj.quaas,obj.moans,obj.tail_flags,obj.tail_twitches,obj.approaches, obj.indifferent, obj.runs_from, obj.other_interactions, obj.lati_long, obj.zip_codes, obj.community_districts, obj.borough_boundaries, obj.city_council_districts, obj.police_precincts])
                
