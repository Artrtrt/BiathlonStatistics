# Generated by Django 4.2 on 2023-04-17 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sportsman', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('gold_medals', models.IntegerField()),
                ('silver_medals', models.IntegerField()),
                ('bronze_medals', models.IntegerField()),
                ('points', models.IntegerField()),
                ('competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions_control.competition')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions_control.season'),
        ),
    ]
