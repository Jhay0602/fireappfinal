# Generated by Django 4.2.11 on 2024-06-01 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0003_alter_firefighters_experience_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firefighters',
            name='experience_level',
            field=models.CharField(choices=[('Probationary Firefighter', 'Probationary Firefighter'), ('Firefighter I', 'Firefighter I'), ('Firefighter II', 'Firefighter II'), ('Firefighter III', 'Firefighter III'), ('Driver', 'Driver'), ('Captain', 'Captain'), ('Battalion Chief', 'Battalion Chief')], max_length=150),
        ),
        migrations.AlterField(
            model_name='firefighters',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='firefighters', to='fire.firestation'),
        ),
    ]
