# Generated by Django 5.0.6 on 2024-05-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_conversation_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='description',
        ),
        migrations.AddField(
            model_name='conversation',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
