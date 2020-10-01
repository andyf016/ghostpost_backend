# Generated by Django 3.1.1 on 2020-10-01 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(choices=[('b', 'Boast'), ('r', 'Roast')], default='b', max_length=10)),
                ('body', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]