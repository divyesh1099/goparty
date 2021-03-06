# Generated by Django 4.0.3 on 2022-05-03 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_restaurant_good_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('great_food', models.BooleanField(default=True)),
                ('satisfactory_staff', models.BooleanField(default=True)),
                ('great_ambience', models.BooleanField(default=True)),
                ('good_service', models.BooleanField(default=True)),
                ('resonable_cost', models.BooleanField(default=True)),
                ('hygiene_and_cleanliness', models.BooleanField(default=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='home.restaurant')),
            ],
        ),
    ]
