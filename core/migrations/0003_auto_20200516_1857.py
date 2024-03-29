# Generated by Django 2.2.6 on 2020-05-16 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200516_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_number_of_your_referral', models.CharField(max_length=2000)),
                ('how_much_you_have', models.CharField(max_length=2000)),
                ('button_status', models.CharField(max_length=2000)),
                ('button_note', models.CharField(max_length=2000)),
                ('your_paypal_email', models.EmailField(max_length=254)),
                ('referred', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Foll',
        ),
    ]
