# Generated by Django 3.2.16 on 2024-06-13 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20240613_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='polls.user'),
        ),
        migrations.AddField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='polls.user'),
        ),
    ]
