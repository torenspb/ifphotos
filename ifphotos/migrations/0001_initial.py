# Generated by Django 2.0 on 2017-12-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=100)),
                ('req_method', models.CharField(default=0, max_length=1)),
                ('search_value', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
