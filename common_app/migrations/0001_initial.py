# Generated by Django 4.1.7 on 2024-11-26 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=40)),
                ('admin_email', models.CharField(max_length=40)),
                ('admin_password', models.CharField(default='', max_length=10)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.BigIntegerField()),
                ('remark', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_description', models.TextField()),
                ('dep_image', models.ImageField(upload_to='department/')),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_mobile', models.BigIntegerField()),
                ('patient_address', models.CharField(max_length=200)),
                ('patient_email', models.CharField(max_length=40)),
                ('patient_password', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='active', max_length=20)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_email', models.CharField(max_length=40)),
                ('doctor_phone', models.BigIntegerField()),
                ('doctor_address', models.CharField(max_length=200)),
                ('user_name', models.IntegerField(default=0)),
                ('password', models.CharField(default='', max_length=40)),
                ('doctor_gender', models.CharField(max_length=15)),
                ('doctor_image', models.ImageField(default='static/images/dummy-user.png', upload_to='doctor/')),
                ('status', models.CharField(default='pending', max_length=20)),
                ('doctor_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_app.departments')),
            ],
            options={
                'db_table': 'doctors',
            },
        ),
    ]
