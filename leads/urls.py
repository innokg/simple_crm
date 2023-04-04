from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
        path('', lead_list, name='lead-list'),
        path('<int:pk>/', lead_detail, name="lead-detail"),        # navigation using lead's pk, always use annotation for types
        path('<int:pk>/update/', lead_update, name="lead-update"), # updating the lead's information
        path('<int:pk>/delete/', lead_delete, name='lead-delete'), # deleting the lead from database
        path('create/', lead_create, name='lead-create'),          #create a new lead
]
