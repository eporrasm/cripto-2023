# Generated by Django 4.2.7 on 2023-11-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField()),
                ('rb', models.IntegerField()),
                ('ga_mod_p', models.IntegerField(blank=True, null=True)),
                ('b', models.IntegerField(blank=True, null=True)),
                ('gb_mod_p', models.IntegerField(blank=True, null=True)),
                ('k', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
