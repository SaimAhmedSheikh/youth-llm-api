# Generated by Django 5.0.6 on 2024-06-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_testresult_reference_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='result_reported',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sample_dated',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sample_received',
            field=models.CharField(max_length=50),
        ),
    ]
