from django.contrib import admin
from django.urls import path

from tarefas.views import TarefasListView, TarefasCreateView, TarefasUpdateView, TarefasDeleteView, TarefasCompletarTarefaView, TarefasMoverTarefaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TarefasListView.as_view(), name="tarefas_list"),
    path('create', TarefasCreateView.as_view(), name="tarefas_create"),
    path('update/<int:pk>', TarefasUpdateView.as_view(), name="tarefas_update"),
    path('delete/<int:pk>', TarefasDeleteView.as_view(), name="tarefas_delete"),
    path('complete/<int:pk>', TarefasCompletarTarefaView.as_view(), name="tarefas_complete"),
    path('tarefas/<int:pk>/mover/<str:direction>', TarefasMoverTarefaView.as_view(), name="tarefas_mover"),
]
