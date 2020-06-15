# Generated by Django 2.1.4 on 2020-06-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AddField(
            model_name='place',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='Свободно ?'),
        ),
    ]