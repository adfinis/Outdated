# Generated by Django 3.2.16 on 2022-11-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('package_release_date', models.DateField()),
                ('package_end_of_life_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_repo', models.CharField(max_length=200)),
                ('packages', models.ManyToManyField(blank=True, to='projects.Package')),
            ],
        ),
    ]