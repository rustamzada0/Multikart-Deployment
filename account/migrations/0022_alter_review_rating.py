# Generated by Django 4.2.6 on 2023-11-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(2, '⭐⭐'), (3, '⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (1, '⭐')], null=True),
        ),
    ]
