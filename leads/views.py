from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from loguru import logger
from .forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# CRUD - Creata, Retrieve, Update, Delete + List




class LandingPageView(TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }  # context is a dictionary of information
    return render(request, "leads/lead_list.html", context)




class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}

    return render(request, "leads/lead_detail.html", context)



class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_create(request):  # sourcery skip: extract-method
    form = LeadModelForm()
    if request.method == 'POST':  # check if form is a POST method
        form = LeadModelForm(request.POST)
        if form.is_valid():  # if form is valid, checking the form
            form.save()  # All this documented code is replaced by one line, because we used a ModelForm
            logger.info(f'{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]} has been added to database')
            return redirect('/leads')
    context = {
        "form": form
        }
    return render(request, "leads/lead_create.html", context)



class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':  # check if form is a POST method
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():  # if form is valid, checking the form
            form.save()
            return redirect('/leads')
    context = {
        "form": form,
        "lead": lead,
        }

    return render(request, "leads/lead_update.html", context)



class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    logger.info(f"Deleting lead {lead}",)
    lead.delete()
    return redirect('/leads')

