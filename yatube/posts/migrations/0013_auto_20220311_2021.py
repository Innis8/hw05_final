# Generated by Django 2.2.16 on 2022-03-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20220311_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Написать комментарий', max_length=350, verbose_name='Текст комментария'),
        ),
    ]