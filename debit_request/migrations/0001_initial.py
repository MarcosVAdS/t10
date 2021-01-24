# Generated by Django 3.1.5 on 2021-01-23 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(max_length=244)),
                ('value', models.CharField(default='0', max_length=244)),
                ('target', models.CharField(max_length=14)),
                ('super_user', models.BooleanField()),
                ('is_enable', models.BooleanField()),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['updated_at'],
            },
        ),
    ]
