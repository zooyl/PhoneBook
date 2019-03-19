from django.shortcuts import render, redirect
from django.views import View
from Book.models import Person, Phone, Email, Group, Address, c_type
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import AddPersonForm, PersonAddressHiddenKey, PersonEmailHiddenKey, PersonPhoneHiddenKey, AddGroupForm
from django.views.generic.edit import DeleteView, UpdateView, CreateView
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


class AddAddress(CreateView):
    form_class = PersonAddressHiddenKey
    model = Address
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['occupant_key'] = self.kwargs['id']
        return initial_data


class AddPhone(CreateView):
    form_class = PersonPhoneHiddenKey
    model = Phone
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['phone_key'] = self.kwargs['id']
        return initial_data


class AddEmail(CreateView):
    form_class = PersonEmailHiddenKey
    model = Email
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['email_key'] = self.kwargs['id']
        return initial_data


class EditBasic(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('home')


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('home')


class AddressDelete(DeleteView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('home')


class PhoneDelete(DeleteView):
    model = Phone
    fields = '__all__'
    success_url = reverse_lazy('home')


class EmailDelete(DeleteView):
    model = Email
    fields = '__all__'
    success_url = reverse_lazy('home')


class GroupDelete(DeleteView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('home')


class AddGroup(View):

    def get(self, request, id):
        groups = Group.objects.all()
        if groups.exists():
            return render(request, "add_group.html", {'groups': groups})
        else:
            empty_group = "There is no group in database"
            return render(request, "display_person.html", {'empty_group': empty_group})

    def post(self, request, id):
        person = Person.objects.get(id=id)
        group_id = request.POST['group']
        selected = Group.objects.get(id=group_id)
        selected.group_key.add(person)
        selected.save()
        return redirect(f'/details/basic/{id}')


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


def group_list(request):
    existing = Group.objects.all()
    return render(request, "group_list.html", {'existing': existing})


class SearchUser(View):

    def get(self, request):
        return render(request, "search.html")

    def post(self, request):
        search = request.POST['search']
        person = Person.objects.filter(name__contains=search)
        return render(request, "search.html", {'person': person})
