# Generated by Django 4.2.1 on 2023-06-15 10:56

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
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField(default='')),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
