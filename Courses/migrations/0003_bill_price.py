# Generated by Django 4.1.7 on 2023-03-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
