# Generated by Django 4.1.3 on 2023-02-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_galeriafoto_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_product', models.CharField(max_length=100)),
            ],
        ),
    ]
