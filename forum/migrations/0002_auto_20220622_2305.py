# Generated by Django 3.2 on 2022-06-22 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumtopics',
            options={'verbose_name_plural': 'Forum Topics'},
        ),
        migrations.AddField(
            model_name='forumpost',
            name='topic',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='forum_posts_topic',
                to='forum.forumtopics'),
        ),
    ]
