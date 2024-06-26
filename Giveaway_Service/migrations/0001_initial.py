# Generated by Django 5.0.3 on 2024-04-28 08:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=100)),
                ('pickup_location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Giveaway_Service.author')),
                ('owner', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Giveaway_Service.genre')),
            ],
        ),
        migrations.CreateModel(
            name='OwnershipDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_recipient', models.BooleanField(default=False)),
                ('book', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='Giveaway_Service.book')),
                ('user', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='interested_users',
            field=models.ManyToManyField(related_name='interested_books', through='Giveaway_Service.OwnershipDecision', to=settings.AUTH_USER_MODEL),
        ),
    ]
