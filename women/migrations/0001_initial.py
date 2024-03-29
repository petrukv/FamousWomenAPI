# Generated by Django 4.2.5 on 2024-01-24 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('time_create', models.DateField(auto_now_add=True)),
                ('time_update', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField()),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category')),
            ],
        ),
    ]
