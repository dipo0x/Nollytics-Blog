# Generated by Django 2.2.6 on 2020-05-16 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20200516_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
