# Generated by Django 3.0.5 on 2020-05-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_userprofile_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, height_field=300, upload_to='', verbose_name='Картинка', width_field=400),
        ),
    ]