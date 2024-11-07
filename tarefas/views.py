from asyncio.windows_events import NULL
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date

from .models import Tarefas

class TarefasListView(ListView):
    model = Tarefas
    ordering = ['ordemDeApresentacao']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarefas_list = self.get_queryset()
        context['listaZerada'] = all(tarefa.ordemDeApresentacao == 0 for tarefa in tarefas_list)
        return context

class TarefasCreateView(CreateView):
    model = Tarefas
    fields = ["nomeTarefa", "dataLimite", "custo"]
    success_url = reverse_lazy('tarefas_list')

class TarefasUpdateView(UpdateView):
    model = Tarefas
    fields = ["nomeTarefa", "dataLimite", "custo"]
    success_url = reverse_lazy('tarefas_list')

class TarefasDeleteView(DeleteView):
    model = Tarefas
    success_url = reverse_lazy('tarefas_list')

class TarefasCompletarTarefaView(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefas, pk=pk)
        tarefa.ordemDeApresentacao = NULL
        tarefa.save()
        return redirect('tarefas_list')

class TarefasMoverTarefaView(View):
    def get(self, request, pk, direction):
        tarefa = get_object_or_404(Tarefas, pk=pk)

        if direction == 'up':
            # Encontra a tarefa imediatamente acima
            tarefa_acima = Tarefas.objects.filter(ordemDeApresentacao=tarefa.ordemDeApresentacao - 1).first()
            if tarefa_acima:
                # Troca as ordens entre a tarefa atual e a tarefa acima
                tarefa_acima.ordemDeApresentacao += 1
                tarefa_acima.save()
            tarefa.ordemDeApresentacao -= 1
            tarefa.save()

        elif direction == 'down':
            # Encontra a tarefa imediatamente abaixo
            tarefa_abaixo = Tarefas.objects.filter(ordemDeApresentacao=tarefa.ordemDeApresentacao + 1).first()
            if tarefa_abaixo:
                # Troca as ordens entre a tarefa atual e a tarefa abaixo
                tarefa_abaixo.ordemDeApresentacao -= 1
                tarefa_abaixo.save()
            tarefa.ordemDeApresentacao += 1
            tarefa.save()

        return redirect('tarefas_list')