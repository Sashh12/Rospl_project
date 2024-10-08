# Generated by Django 5.1.1 on 2024-09-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('ProductId', models.CharField(max_length=20)),
                ('food_name', models.CharField(max_length=100)),
                ('food_category', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
