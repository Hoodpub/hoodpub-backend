# Generated by Django 2.0.1 on 2018-01-29 11:52

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hoodpub', '0004_user_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_profile',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/user/', verbose_name='Image'),
        ),
    ]