# Generated by Django 3.0.5 on 2020-06-15 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0035_auto_20200615_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='block',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_block', to='questions.QuestionInBlock', verbose_name='Блок'),
        ),
    ]
