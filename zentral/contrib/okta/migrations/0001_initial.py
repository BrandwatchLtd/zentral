# Generated by Django 2.2.3 on 2019-08-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okta_domain', models.CharField(max_length=256)),
                ('api_token', models.CharField(max_length=256)),
                ('okta_id', models.CharField(max_length=256, null=True)),
                ('name', models.CharField(max_length=256)),
                ('authorization_key', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'unique_together': {('okta_domain', 'name')},
            },
        ),
    ]