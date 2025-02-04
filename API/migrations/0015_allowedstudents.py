# Generated by Django 3.1.6 on 2021-05-08 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0014_examresults_studentanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.exam')),
                ('students', models.ManyToManyField(to='API.Student')),
            ],
        ),
    ]
