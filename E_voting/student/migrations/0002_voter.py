# Generated by Django 5.0 on 2023-12-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('grader', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('city', models.IntegerField()),
                ('region', models.IntegerField()),
            ],
        ),
    ]