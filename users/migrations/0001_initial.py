# Generated by Django 3.1.1 on 2020-09-08 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('national_code', models.CharField(max_length=11, unique=True, verbose_name='national code')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('perm', models.BooleanField(default=True)),
                ('complete', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=20)),
                ('birthPlace', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=1)),
                ('phone_number', models.CharField(max_length=17)),
                ('email', models.EmailField(max_length=25)),
                ('province', models.CharField(max_length=18)),
                ('city', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=40)),
                ('education', models.CharField(max_length=1)),
                ('field', models.CharField(blank=True, max_length=20)),
                ('university', models.CharField(blank=True, max_length=20)),
                ('studentNumber', models.CharField(max_length=1)),
                ('religousEducation', models.CharField(max_length=20)),
                ('englishLanguage', models.IntegerField(default=0)),
                ('arabicLanguage', models.IntegerField(default=0)),
                ('fisically', models.IntegerField(default=0)),
                ('defective', models.CharField(blank=True, max_length=40)),
                ('disease', models.CharField(blank=True, max_length=15)),
                ('drugs', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
