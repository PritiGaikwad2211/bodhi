# Generated by Django 3.2.4 on 2021-06-24 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bodhitech', '0009_auto_20210623_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='Description_1',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='Heading_1',
            new_name='Heading',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='Img_1',
            new_name='Img',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='img1',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='Title_1',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='content_1',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='gif_1',
            new_name='gif',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Description_2',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Description_3',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Description_4',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Heading_2',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Heading_3',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Heading_4',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Img_2',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Img_3',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='Img_4',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img5',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img6',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img7',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='img8',
        ),
        migrations.RemoveField(
            model_name='section',
            name='Title_2',
        ),
        migrations.RemoveField(
            model_name='section',
            name='Title_3',
        ),
        migrations.RemoveField(
            model_name='section',
            name='Title_4',
        ),
        migrations.RemoveField(
            model_name='section',
            name='Title_5',
        ),
        migrations.RemoveField(
            model_name='section',
            name='Title_6',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content_2',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content_3',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content_4',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content_5',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content_6',
        ),
        migrations.RemoveField(
            model_name='section',
            name='gif_2',
        ),
        migrations.RemoveField(
            model_name='section',
            name='gif_3',
        ),
        migrations.RemoveField(
            model_name='section',
            name='gif_4',
        ),
        migrations.RemoveField(
            model_name='section',
            name='gif_5',
        ),
        migrations.RemoveField(
            model_name='section',
            name='gif_6',
        ),
    ]