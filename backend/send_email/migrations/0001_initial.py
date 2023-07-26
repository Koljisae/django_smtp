# Generated by Django 4.2.3 on 2023-07-26 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_mail', models.BooleanField(default=False, help_text='I want to receive mails.', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_contact', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Contact',
                'verbose_name_plural': 'Users Contacts',
                'ordering': ['user'],
            },
        ),
    ]
