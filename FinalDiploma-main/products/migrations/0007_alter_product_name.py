# Generated by Django 4.2.1 on 2023-06-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productcategory_product_discount_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
