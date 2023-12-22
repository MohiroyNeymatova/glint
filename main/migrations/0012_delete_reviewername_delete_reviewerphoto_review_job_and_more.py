# Generated by Django 4.1.6 on 2023-09-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_project_delete_authorphoto_delete_authorwords_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewerName',
        ),
        migrations.DeleteModel(
            name='ReviewerPhoto',
        ),
        migrations.AddField(
            model_name='review',
            name='job',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(default=5, upload_to='reviews/'),
            preserve_default=False,
        ),
    ]