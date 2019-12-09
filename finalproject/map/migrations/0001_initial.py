# Generated by Django 2.2.7 on 2019-12-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, help_text='latitude', max_digits=20)),
                ('longtitude', models.DecimalField(decimal_places=10, help_text='longitude', max_digits=20)),
                ('unique_squirrel_id', models.CharField(default=None, help_text='Unique Squirrel ID', max_length=200)),
                ('hectare', models.CharField(default=None, help_text='Hectare', max_length=16)),
                ('hectare_squirrel_number', models.IntegerField(default=None, help_text='Hectare squirrel number ')),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='shift', max_length=16)),
                ('date', models.DateField(default=None, help_text='Date')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='Adult', help_text='age', max_length=16)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'black')], default='Black', help_text='primary fur color', max_length=16)),
                ('highlight_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'black'), ('White', 'White')], default='Black', help_text='primary fur color', max_length=16)),
                ('combination', models.CharField(default='Gray+', help_text='combination', max_length=200)),
                ('color_notes', models.CharField(blank=True, default='', help_text='Color notes', max_length=200, null=True)),
                ('location', models.CharField(choices=[('Ground plane', 'Ground plane'), ('Above ground', 'Above ground')], default='Ground plane', help_text='location', max_length=16)),
                ('above_ground_sighter_measurement', models.CharField(default=False, help_text='Above Ground Sighter Measurement', max_length=9)),
                ('specific_location', models.CharField(default=None, help_text='specific location', max_length=100)),
                ('running', models.BooleanField(default=False, help_text='running')),
                ('chasing', models.BooleanField(default=False, help_text='chasing')),
                ('climbing', models.BooleanField(default=False, help_text='climbing')),
                ('eating', models.BooleanField(default=False, help_text='eating')),
                ('foraging', models.BooleanField(default=False, help_text='foraging')),
                ('other_activities', models.CharField(default=None, help_text='other activities', max_length=100)),
                ('kuks', models.BooleanField(default=False, help_text='kuks')),
                ('quaas', models.BooleanField(default=False, help_text='quaas')),
                ('moans', models.BooleanField(default=False, help_text='moans')),
                ('tail_flags', models.BooleanField(default=False, help_text='tail flags')),
                ('tail_twitches', models.BooleanField(default=False, help_text='tail twitches')),
                ('approaches', models.BooleanField(default=False, help_text='approaches')),
                ('indifferent', models.BooleanField(default=False, help_text='indifferent')),
                ('runs_from', models.BooleanField(default=False, help_text='runs from')),
                ('other_interactions', models.CharField(default=None, help_text='other interactions', max_length=100)),
                ('lati_long', models.CharField(default=None, help_text='lati_long', max_length=100)),
                ('zip_codes', models.CharField(default=None, help_text='zip codes', max_length=100)),
                ('community_districts', models.CharField(default=None, help_text='Community Districts', max_length=10)),
                ('borough_boundaries', models.CharField(default=None, help_text='Borough Boundaries', max_length=10)),
                ('city_council_districts', models.CharField(default=None, help_text='City Council Districts', max_length=10)),
                ('police_precincts', models.CharField(default=None, help_text='Police Precincts', max_length=10)),
            ],
        ),
    ]
