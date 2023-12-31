# Generated by Django 4.2.6 on 2023-12-14 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deposit',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.budget'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.budget'),
            preserve_default=False,
        ),
    ]
