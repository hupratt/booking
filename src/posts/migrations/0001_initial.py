# Generated by Django 3.0.1 on 2019-12-24 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import klingon.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField()),
                ('slug', models.SlugField(default='event', unique=True)),
                ('tag', models.CharField(default='event', max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('draft', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
            bases=(models.Model, klingon.models.Translatable),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('alt', models.CharField(blank=True, max_length=120, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.Post')),
            ],
        ),
    ]