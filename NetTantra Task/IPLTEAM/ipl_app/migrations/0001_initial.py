# Generated by Django 3.2.10 on 2021-12-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=100, null=True)),
                ('team_icon', models.FileField(null=True, upload_to='media/ticon/')),
                ('team_player_count', models.IntegerField(blank=True, null=True)),
                ('team_top_bat', models.CharField(blank=True, max_length=500, null=True)),
                ('team_top_bowl', models.CharField(blank=True, max_length=500, null=True)),
                ('team_won_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
