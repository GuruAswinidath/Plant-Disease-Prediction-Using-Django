# Generated by Django 3.2.16 on 2024-12-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_auto_20241220_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('place', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
