# Generated by Django 5.1 on 2024-08-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitem_available_alter_menuitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]