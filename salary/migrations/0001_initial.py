# Generated by Django 4.2.5 on 2023-09-15 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_who_get_salary', to='accounts.staff')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_who_pay_others', to='accounts.staff')),
            ],
        ),
    ]