# Generated by Django 4.2.16 on 2024-10-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_string', models.CharField(max_length=255)),
                ('ast', models.TextField()),
            ],
        ),
    ]