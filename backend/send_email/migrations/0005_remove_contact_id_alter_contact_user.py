# Generated by Django 4.2.3 on 2023-07-27 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('send_email', '0004_alter_contact_subscribed_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='user_contact', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
