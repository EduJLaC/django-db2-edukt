# Generated by Django 3.0.8 on 2020-07-21 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_delete_reinforce'),
        ('questionnaire', '0003_auto_20200719_1506'),
        ('subscription', '0008_auto_20200717_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reinforce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Course')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.BooleanField(default=False)),
                ('score', models.DecimalField(decimal_places=3, max_digits=7)),
                ('good', models.IntegerField()),
                ('bad', models.IntegerField()),
                ('date_done', models.DateField()),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questionnaire.Questionnaire')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
