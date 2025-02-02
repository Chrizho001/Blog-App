# Generated by Django 5.1 on 2024-09-11 20:41

import datetime
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_message_created_alter_message_last_name'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 20, 41, 56, 697525, tzinfo=datetime.timezone.utc)),
        ),
    ]
