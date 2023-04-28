# Generated by Django 4.2 on 2023-04-28 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('browserGame', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actionlog',
            name='attacker',
        ),
        migrations.RemoveField(
            model_name='actionlog',
            name='victim',
        ),
        migrations.AddField(
            model_name='actionlog',
            name='performer',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, related_name='performer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actionlog',
            name='target',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, related_name='target', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]