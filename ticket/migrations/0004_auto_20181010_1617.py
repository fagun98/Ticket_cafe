# Generated by Django 2.1.2 on 2018-10-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_ticketbuy_moviename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketbuy',
            name='moviename',
            field=models.CharField(choices=[('IM', 'IRONMAN'), ('HCS', 'HOME COMING SPIDERMAN'), ('TGF', 'THE GODFATHER'), ('MI:F', 'MISSION IMPOSSIBLE FALLOUT'), ('FF', 'FAST-FIVE'), ('GG', 'GONE GIRL'), ('LO', 'LOGAN'), ('SW', 'STARWARS'), ('IN', 'INCEPTION')], max_length=4),
        ),
    ]
