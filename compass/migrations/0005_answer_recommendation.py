# Generated by Django 2.0.4 on 2018-04-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0004_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='recommendation',
            field=models.TextField(default='Contact Anish Patel for more information'),
        ),
    ]
