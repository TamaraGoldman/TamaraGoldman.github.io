# Generated by Django 3.0.7 on 2020-09-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(verbose_name='Отзыв')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
