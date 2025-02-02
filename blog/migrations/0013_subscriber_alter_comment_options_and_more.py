# Generated by Django 5.1 on 2024-09-15 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_posts_tags_alter_message_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-subscribed_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveIndex(
            model_name='message',
            name='blog_messag_name_4345eb_idx',
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['-created'], name='blog_messag_created_84f231_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriber',
            index=models.Index(fields=['-subscribed_at'], name='blog_subscr_subscri_7a832f_idx'),
        ),
    ]
