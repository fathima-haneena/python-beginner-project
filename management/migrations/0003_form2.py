# Generated by Django 4.2.7 on 2023-11-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_form1'),
    ]

    operations = [
        migrations.CreateModel(
            name='form2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
