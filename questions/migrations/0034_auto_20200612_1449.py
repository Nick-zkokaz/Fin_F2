# Generated by Django 3.0.5 on 2020-06-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0033_userprofile_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='is_passed',
            field=models.BooleanField(default=False, help_text='Поставте галочку, для деактивации теста', verbose_name='Сделать тест недоступным'),
        ),
    ]