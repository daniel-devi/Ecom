# Generated by Django 4.2.6 on 2023-10-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_image1_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='img/placeholder.png', null=True, upload_to='uploads'),
        ),
    ]
