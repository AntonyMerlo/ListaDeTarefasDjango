from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now
def valideData(value):
    if value < now().date():
        raise ValidationError("A data limite não pode ser anterior ao dia de hoje.")

class Tarefas(models.Model):
    idTarefas = models.AutoField(primary_key=True)
    nomeTarefa = models.CharField(verbose_name="Nome da tarefa", max_length=40, unique=True, null=False, blank=False)
    custo = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=False, validators=[MinValueValidator(0)], default=0)
    dataLimite = models.DateField(verbose_name="Data de Limite", null=False, blank=False, validators=[valideData])
    ordemDeApresentacao = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.ordemDeApresentacao is None:
            last_order = Tarefas.objects.all().order_by('-ordemDeApresentacao').first()
            if last_order and last_order.ordemDeApresentacao is not None:
                self.ordemDeApresentacao = last_order.ordemDeApresentacao + 1
            else:
                self.ordemDeApresentacao = 1
        super(Tarefas, self).save(*args, **kwargs)
