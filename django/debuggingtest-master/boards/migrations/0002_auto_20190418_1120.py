# Generated by Django 2.1.8 on 2019-04-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boards.Board'),
            preserve_default=False,
        ),
    ]
