# Generated by Django 3.2.7 on 2022-01-14 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cbc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rbc', models.FloatField()),
                ('wbc', models.FloatField()),
                ('pc', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
