# Generated by Django 3.0.1 on 2020-01-01 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('alt', models.CharField(default='blank', max_length=120)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='room_image', to='rooms.Room')),
            ],
        ),
    ]
