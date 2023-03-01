# Generated by Django 4.1.5 on 2023-02-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'UserInformation',
            },
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
