# Generated by Django 4.2.6 on 2023-11-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐')], null=True),
        ),
    ]
