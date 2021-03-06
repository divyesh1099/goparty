# Generated by Django 4.0.3 on 2022-04-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_restaurantimage_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='edited',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
