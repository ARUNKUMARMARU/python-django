# Generated by Django 5.0.6 on 2024-05-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_conversation_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]