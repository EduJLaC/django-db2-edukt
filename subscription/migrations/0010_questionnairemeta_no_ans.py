# Generated by Django 3.0.8 on 2020-07-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0009_questionnairemeta_reinforce'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnairemeta',
            name='no_ans',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]