# Generated by Django 5.0.6 on 2024-06-08 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_rename_results_scrapingjob_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapingjob',
            old_name='tasks',
            new_name='results',
        ),
    ]