# Generated by Django 2.0.2 on 2018-03-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
