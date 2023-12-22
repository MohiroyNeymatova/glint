# Generated by Django 4.1.6 on 2023-09-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_reviewername_delete_reviewerphoto_review_job_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='FirstName',
        ),
        migrations.DeleteModel(
            name='LastName',
        ),
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default=5, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='first_name',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='last_name',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
    ]
