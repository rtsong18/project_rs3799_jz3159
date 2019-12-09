from django.forms import ModelForm
from map.models import squirrels

class squirrels_form(ModelForm):
    class Meta:
        model = squirrels
        fields = '__all__'

