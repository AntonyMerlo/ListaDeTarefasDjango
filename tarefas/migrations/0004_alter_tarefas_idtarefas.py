# Generated by Django 5.1.2 on 2024-11-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0003_alter_tarefas_custo_alter_tarefas_datalimite"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefas",
            name="idTarefas",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]