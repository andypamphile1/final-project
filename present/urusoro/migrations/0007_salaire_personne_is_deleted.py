# Generated by Django 4.2 on 2024-04-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urusoro', '0006_alter_presence_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=31)),
                ('salaire', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='personne',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
