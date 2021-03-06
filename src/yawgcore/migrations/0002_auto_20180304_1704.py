# Generated by Django 2.0.2 on 2018-03-04 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('yawgcore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=128)),
                ('album_alias', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=128)),
                ('filename', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ItemMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.PositiveIntegerField()),
                ('item_id', models.PositiveIntegerField()),
                ('item_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mapping_item', to='contenttypes.ContentType')),
                ('parent_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mapping_parent', to='contenttypes.ContentType')),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_alias',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='gallerydomainmap',
            name='domain_host',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
