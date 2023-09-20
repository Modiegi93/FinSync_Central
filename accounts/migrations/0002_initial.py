# Generated by Django 4.2.5 on 2023-09-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='workplaces',
            field=models.ManyToManyField(related_name='workplace_of_staff', to='companies.company'),
        ),
    ]