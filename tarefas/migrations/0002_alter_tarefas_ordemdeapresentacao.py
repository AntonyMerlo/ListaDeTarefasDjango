# Generated by Django 5.1.2 on 2024-11-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefas",
            name="ordemDeApresentacao",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
