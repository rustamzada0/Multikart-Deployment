# Generated by Django 4.2.6 on 2023-11-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_detail_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_detail_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]