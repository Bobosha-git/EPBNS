# Generated by Django 5.1.5 on 2025-02-01 16:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
