# Generated by Django 4.0.3 on 2022-05-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featureds', to='home.restaurant')),
            ],
        ),
    ]
