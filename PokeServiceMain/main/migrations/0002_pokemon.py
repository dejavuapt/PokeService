# Generated by Django 4.2.7 on 2023-11-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('poke_id', models.IntegerField()),
                ('picture_url', models.CharField(max_length=200)),
                ('back_picture_url', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('types_of_attack', models.CharField(max_length=200)),
            ],
        ),
    ]