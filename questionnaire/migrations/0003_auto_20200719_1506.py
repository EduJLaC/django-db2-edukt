# Generated by Django 3.0.8 on 2020-07-19 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('questionnaire', '0002_auto_20200718_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reinforce',
            name='course',
        ),
        migrations.RemoveField(
            model_name='reinforce',
            name='subscriber',
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Topic'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Reinforce',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
