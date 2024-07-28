# Generated by Django 3.1.6 on 2021-05-14 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0018_errormessages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_duration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_startdate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.examiner'),
        ),
    ]
