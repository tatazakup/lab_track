# Generated by Django 3.0.3 on 2020-06-11 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kmutnbtrackapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('name', models.CharField(max_length=300, null=True)),
                ('amount', models.IntegerField(blank=True)),
                ('hash', models.CharField(default=kmutnbtrackapp.models.create_id, max_length=16, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('student_id', models.CharField(blank=True, default='', max_length=13)),
                ('is_student', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField(auto_now_add=True, null=True)),
                ('checkout', models.DateTimeField(null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmutnbtrackapp.Lab')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmutnbtrackapp.Person')),
            ],
        ),
    ]