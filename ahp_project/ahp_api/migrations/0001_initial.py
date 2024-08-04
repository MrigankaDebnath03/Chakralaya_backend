# Generated by Django 5.0.6 on 2024-08-03 11:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AHPProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('criteria', models.JSONField()),
                ('alternatives', models.JSONField()),
                ('pairwise_matrix', models.JSONField()),
                ('alternative_matrices', models.JSONField()),
                ('ranking_data', models.JSONField()),
                ('ranking_list', models.JSONField()),
                ('alternative_scores', models.JSONField()),
                ('weights', models.JSONField()),
                ('consistency_ratio', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]