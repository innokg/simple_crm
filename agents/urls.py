from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetalView, AgentUpdateView,  AgentDeleteView


app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('<int:pk>/', AgentDetalView.as_view(), name="agent-detail"),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name="agent-update"), # updating the agent's information
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'), # deleting the agent from database
]
