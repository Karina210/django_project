# Generated by Django 3.2 on 2021-05-04 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='contact_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='home.contactinfo'),
        ),
    ]
