from django.forms import ModelForm
from .models import Person


class AddPerson(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
