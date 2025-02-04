# Generated by Django 3.1.6 on 2021-06-06 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0024_auto_20210518_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSupervisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.exam')),
                ('supervisor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.supervisor')),
            ],
        ),
    ]
