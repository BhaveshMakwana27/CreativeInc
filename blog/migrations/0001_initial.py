# Generated by Django 4.2.3 on 2023-07-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=50)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]
