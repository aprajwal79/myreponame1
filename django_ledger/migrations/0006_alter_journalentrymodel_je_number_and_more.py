# Generated by Django 4.1.5 on 2023-02-17 19:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0005_remove_itemmodel_django_ledg_invento_dbf206_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentrymodel',
            name='je_number',
            field=models.SlugField(editable=False, max_length=25, verbose_name='Journal Entry Number'),
        ),
        migrations.AlterField(
            model_name='journalentrymodel',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Timestamp'),
        ),
    ]
