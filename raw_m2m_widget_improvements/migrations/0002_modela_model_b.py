# Generated by Django 2.0.dev20170812190649 on 2017-08-15 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw_m2m_widget_improvements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modela',
            name='model_b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='foos', to='raw_m2m_widget_improvements.ModelB'),
        ),
    ]