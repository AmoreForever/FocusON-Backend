# Generated by Django 3.1.6 on 2021-04-13 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_auto_20210414_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='previous_question',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.question'),
        ),
    ]
