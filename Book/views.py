from django.shortcuts import render, redirect
from django.views import View
from Book.models import Person, Phone, Email, Group, c_type
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import AddPersonForm, PersonAddressForm, PersonEmailForm, PersonPhoneForm, AddGroupForm
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy


def home(request):
    person = Person.objects.all().order_by('name')
    if person.exists():
        return render(request, "display_person.html", {'person': person})
    else:
        empty_db = "You don't have any contacts"
        return render(request, "display_person.html", {'person': person, 'empty_db': empty_db})


class NewBasic(View):

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'add_basic.html', {'form': form})

    def post(self, request):
        form = AddPersonForm(request.POST)
        if form.is_valid():
            form.save()
            last = Person.objects.latest('id')
            return redirect(f'/details/basic/{last.id}')


class EditBasic(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('home')


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('home')


class AddAddress(View):

    def get(self, request, id):
        address_form = PersonAddressForm(initial={'occupant_key': id})
        return render(request, "add_address.html", {'address_form': address_form})

    def post(self, request, id):
        address_form = PersonAddressForm(request.POST)
        if address_form.is_valid():
            address_form.save()
        return redirect(f'/details/basic/{id}')


class AddPhone(View):

    def get(self, request, id):
        phone_form = PersonPhoneForm(initial={'phone_key': id})
        return render(request, "add_phone.html", {'phone_form': phone_form})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        phone_form = PersonPhoneForm(request.POST)
        if phone_form.is_valid():
            number = phone_form.cleaned_data['number']
            type = phone_form.cleaned_data['type']
            Phone.objects.create(number=number, type=type, phone_key=person)
        return redirect(f'/details/basic/{id}')


class AddEmail(View):

    def get(self, request, id):
        email_form = PersonEmailForm(initial={'email_key': id})
        return render(request, "add_email.html", {'email_form': email_form})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        email_form = PersonEmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            email_type = email_form.cleaned_data['email_type']
            Email.objects.create(email=email, email_type=email_type, email_key=person)
        return redirect(f'/details/basic/{id}')


class AddGroup(View):

    def get(self, request, id):
        groups = Group.objects.all()
        return render(request, "add_group.html", {'groups': groups})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        group_id = request.POST['group']
        selected = Group.objects.get(id=group_id)
        selected.group_key.add(person)
        selected.save()
        return redirect(f'/details/basic/{id}')


def basic_details(request, id):
    person = Person.objects.get(id=id)
    return render(request, "basic_details.html", {'person': person})


def full_details(request, id):
    try:
        person = Person.objects.get(id=id)
        address = person.occupant_key.all()
        email = person.email_key.all()
        phone = person.phone_key.all()
        group = Group.objects.filter(group_key=id)
        return render(request, "details.html", {'id': id, 'person': person, 'address': address,
                                                'email': email, 'phone': phone, "c_type": c_type, 'group': group})
    except ObjectDoesNotExist:
        raise Http404("This person does not have additional information")


class CreateGroup(View):

    def get(self, request):
        group_form = AddGroupForm()
        return render(request, "group.html", {'group_form': group_form})

    def post(self, request):
        group_form = AddGroupForm(request.POST)
        if group_form.is_valid():
            group_form.save()
        success = "Group successfully created"
        return render(request, "success.html", {'success': success})


def group_list(request):
    existing = Group.objects.all()
    return render(request, "group_list.html", {'existing': existing})


def group_details(request, id):
    # XD = Group.group_key.all()
    person = Person.objects.get(id=id)
    group = person.group_key.all()
    print(group)
    # pasod = Group.objects.filter(group_key=XD)
    # print(XD)
    return render(request, "group_details.html")




    # EDIT PERSON POST
    # def post(self, request, id):
    #     advanced = Person.objects.get(id=id)
    #     form_person = AddPersonForm(request.POST, instance=advanced)
    #     form_address = PersonAddressForm(request.POST)
    #     form_phone = PersonPhoneForm(request.POST)
    #     form_email = PersonEmailForm(request.POST)
    #     group_id = request.POST['group']
    #     selected = Group.objects.get(id=group_id)
    #     if form_person.is_valid():
    #         form_person.save()
    #         selected.group_key.add(advanced)
    #         selected.save()
    #     if form_address.is_valid():
    #         form_address.save()
    #     try:
    #         if form_phone.is_valid():
    #             number = form_phone.cleaned_data['number']
    #             type = form_phone.cleaned_data['type']
    #             Phone.objects.create(number=number, type=type, phone_key=advanced)
    #         if form_email.is_valid():
    #             email = form_email.cleaned_data['email']
    #             email_type = form_email.cleaned_data['email_type']
    #             Email.objects.create(email=email, email_type=email_type, email_key=advanced)
    #         return redirect(f'/details/basic/{id}')
    #     except IntegrityError:
    #         return redirect(f'/edit/{id}')
