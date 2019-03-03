from django.shortcuts import render, redirect
from django.views import View
from Book.models import Person, Phone, Email, Address, Group
from django.db import IntegrityError, DataError


def home(request):
    person = Person.objects.all().order_by('name')
    if person.exists():
        return render(request, "display_person.html", {'person': person})
    else:
        empty_db = "You don't have any contacts"
        return render(request, "display_person.html", {'person': person, 'empty_db': empty_db})


class NewBasic(View):

    def get(self, request):
        return render(request, 'add_basic.html')

    def post(self, request):
        Person.objects.create(name=request.POST['name'], surname=request.POST['surname'],
                              description=request.POST['description'])
        last = Person.objects.latest('id')
        return redirect(f'/details/basic/{last.id}')


class NewAdvanced(View):

    def get(self, request, id):
        advanced = Person.objects.get(id=id)
        return render(request, 'edit_person.html', {'advanced': advanced})

    def post(self, request):
        try:
            id = request.POST['id']
            name = request.POST['name']
            surname = request.POST['surname']
            description = request.POST['description']
            # if request is None:
            # Edit for basic informations
            edit = Person.objects.get(id=id)
            edit.name = name
            edit.surname = surname
            edit.description = description
            edit.save()
            Address.objects.create(city=request.POST['city'], street=request.POST['street'],
                                   house_nr=request.POST['house_nr'], flat_nr=request.POST['flat_nr'],
                                   occupant_key=edit)
            Email.objects.create(email=request.POST['email'], email_key=edit)
            Phone.objects.create(number=request.POST['phone_number'], phone_key=edit)
            Group.objects.create(name=request.POST['group'])
            added = "Person added"
            return render(request, "back_button.html", {'added': added})
        except IntegrityError:
            unique = "E-mail already taken, it must be unique"
            return render(request, "edit_person.html", {'unique': unique})
        except DataError:
            number = "Number out of range"
            return render(request, "edit_person.html", {'number': number})


def basic_details(request, id):
    person = Person.objects.get(id=id)
    return render(request, "basic_details.html", {'person': person})

def full_details(request, id):
    person = Person.objects.get(id=id)
    address = Address.objects.get(id=id)
    email = Email.objects.get(id=id)
    phone = Phone.objects.get(id=id)
    group = Group.objects.get(id=id)
    if request.method == "POST":
        if request.POST == ['delete']: # to nie ma sensu i 77
            person.delete()
            redirect("/")
        elif request.POST == ['edit']:
            render(request, 'edit_person.html')
    else:
        return render(request, "details.html", {'id': id, 'person': person, 'address': address,
                                                'email': email, 'phone': phone, 'group': group})
