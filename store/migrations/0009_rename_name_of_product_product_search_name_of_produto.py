# Generated by Django 4.1.3 on 2023-02-02 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_search',
            old_name='name_of_product',
            new_name='name_of_produto',
        ),
    ]
