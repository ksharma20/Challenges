# Generated by Django 4.0.1 on 2022-05-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dtype', models.CharField(max_length=50)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]