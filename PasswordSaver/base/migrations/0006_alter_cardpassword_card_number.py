# Generated by Django 4.0.3 on 2022-08-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_cardpassword_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpassword',
            name='card_number',
            field=models.CharField(max_length=19),
        ),
    ]
