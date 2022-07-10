# Generated by Django 3.2 on 2022-06-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_auto_20220628_0231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='existinguserscontactdetails',
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Existing Users Contact Details'
            },
        ),
        migrations.AlterModelOptions(
            name='siteuserscontactdetails',
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Site Users Contact Details'
            },
        ),
        migrations.AddField(
            model_name='existinguserscontactdetails',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'),
                                               (1, 'Completed')],
                                      default=0),
        ),
        migrations.AddField(
            model_name='siteuserscontactdetails',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'),
                                               (1, 'Completed')],
                                      default=0),
        ),
    ]
