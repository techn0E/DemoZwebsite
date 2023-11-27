# Generated by Django 4.2.7 on 2023-11-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeBudget', '0005_earning_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]