# Generated by Django 3.0.4 on 2020-03-26 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='professor',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]