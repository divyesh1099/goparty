# Generated by Django 4.0.3 on 2022-05-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_restaurant_date_remove_restaurant_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
