# Generated by Django 2.1.7 on 2019-03-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20190309_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_key',
            field=models.ManyToManyField(related_name='User', to='Book.Person'),
        ),
    ]