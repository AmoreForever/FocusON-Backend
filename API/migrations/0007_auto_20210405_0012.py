# Generated by Django 3.1.6 on 2021-04-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20210215_0102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teacher',
            new_name='Examiner',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'student'), ('2', 'examiner'), ('3', 'supervisor')], default='1', max_length=10),
        ),
    ]
