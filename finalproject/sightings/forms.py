from django.forms import ModelForm
from map.models import squirrels

class squirrels_form(ModelForm):
    class META:
        model = squirrels
        fields = '__all__'

