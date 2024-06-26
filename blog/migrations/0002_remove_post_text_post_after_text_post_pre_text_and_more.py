# Generated by Django 4.2.13 on 2024-06-18 19:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='after_text',
            field=ckeditor.fields.RichTextField(default='...'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pre_text',
            field=ckeditor.fields.RichTextField(default='...'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
