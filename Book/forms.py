import django.forms as forms
from django.forms import ModelForm
from .models import Person, Address, c_type, e_type, Group


class AddPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class PersonAddressForm(ModelForm):
    class Meta:
        model = Address
        widgets = {'occupant_key': forms.HiddenInput()}
        fields = '__all__'


class PersonPhoneForm(forms.Form):
    number = forms.IntegerField(label="Number", required=False)
    type = forms.ChoiceField(label="Type", choices=c_type)
    phone_key = forms.IntegerField(widget=forms.HiddenInput)


class PersonEmailForm(forms.Form):
    email = forms.EmailField(label="Email", required=False,
                             error_messages={'unique': "This email has already been registered."})
    email_type = forms.ChoiceField(label="Type", choices=e_type)
    email_key = forms.IntegerField(widget=forms.HiddenInput)


class AddGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']
