# Generated by Django 4.0.3 on 2022-08-26 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_cardpassword_bank_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardpassword',
            name='note',
        ),
    ]