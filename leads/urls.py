from django.urls import path
from .views import ( 
                    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
)
app_name = "leads"

urlpatterns = [
        path('', LeadListView.as_view(), name='lead-list'),
        path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),        # navigation using lead's pk, always use annotation for types
        path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"), # updating the lead's information
        path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'), # deleting the lead from database
        path('create/', LeadCreateView.as_view(), name='lead-create'),          #create a new lead
]
