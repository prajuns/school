# Generated by Django 4.2.3 on 2023-07-31 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('purpose', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
            ],
        ),
    ]
