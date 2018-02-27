# Generated by Django 2.0.2 on 2018-02-25 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=128)),
                ('gallery_alias', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryDomainMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_host', models.CharField(max_length=128)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yawgcore.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('path', models.CharField(max_length=256)),
            ],
        ),
    ]
