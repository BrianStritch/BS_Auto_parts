# Generated by Django 3.2 on 2022-06-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20220623_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumcategory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='forumtopics',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]