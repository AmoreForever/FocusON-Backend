# Generated by Django 3.1.6 on 2021-02-14 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='API.user')),
            ],
        ),
    ]
