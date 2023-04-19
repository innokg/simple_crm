from django import forms
from leads.models import Agent



class AgentmodelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
