# Generated by Django 4.0.2 on 2022-02-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_googlemap_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlemap',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]