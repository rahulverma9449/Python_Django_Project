# Generated by Django 5.0.1 on 2024-02-02 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Stid', to='vege.studentid'),
        ),
    ]