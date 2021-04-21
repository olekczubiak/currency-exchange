# Generated by Django 3.2 on 2021-04-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('website', models.CharField(max_length=100)),
                ('my_id', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('buy_EUR', models.CharField(max_length=100)),
                ('sell_EUR', models.CharField(max_length=100)),
                ('buy_GBP', models.CharField(max_length=100)),
                ('sell_GBP', models.CharField(max_length=100)),
                ('buy_CHF', models.CharField(max_length=100)),
                ('sell_CHF', models.CharField(max_length=100)),
                ('buy_USD', models.CharField(max_length=100)),
                ('sell_USD', models.CharField(max_length=100)),
            ],
        ),
    ]
