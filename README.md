# PhoneBook
PhoneBook helps you organize your phonebook contacts. You can store your friends addresses, phone numbers and emails.

### Installing

These instructions will get you a copy of the project up and running.
Create virtual environment on your machine, then install requirements using:

```
pip install -r requirements.txt
```
### Important
In ```PhoneBook``` folder, update ```local_settings.py.txt```  to your settings and delete ```.txt``` from the end
of a file.

Open terminal in ```manage.py``` directory and type ```python manage.py migrate```.
You can fill database if you want using ```python manage.py loaddata test-contacts```. At last you can start server by ```python manage.py runserver``` command.

### Preview
## Main Page:

![Main](https://github.com/zooyl/PhoneBook/blob/master/preview/ContactList.png?raw=true)

## Details of a contact:

![Details](https://github.com/zooyl/PhoneBook/blob/master/preview/ContactDetails.png?raw=true)

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/)
