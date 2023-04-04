from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from loguru import logger
from .forms import LeadForm, LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }  # context is a dictionary of information
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}

    return render(request, "leads/lead_detail.html", context)


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


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    logger.info(f"Deleting lead {lead}",)
    lead.delete()
    return redirect('/leads')

