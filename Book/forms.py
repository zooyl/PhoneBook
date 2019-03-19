import django.forms as forms
from django.forms import ModelForm
from .models import Person, Address, Phone, Email, Group


class AddPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class PersonAddressHiddenKey(ModelForm):
    class Meta:
        model = Address
        widgets = {'occupant_key': forms.HiddenInput()}
        fields = '__all__'


class PersonPhoneHiddenKey(ModelForm):
    class Meta:
        model = Phone
        widgets = {'phone_key': forms.HiddenInput()}
        fields = '__all__'


class PersonEmailHiddenKey(ModelForm):
    class Meta:
        model = Email
        widgets = {'email_key': forms.HiddenInput()}
        fields = '__all__'


class AddGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']
