# Generated by Django 3.0.8 on 2020-08-11 16:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]