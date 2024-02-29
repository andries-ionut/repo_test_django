from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from servicii.forms import ServiciiForm
from servicii.models import ServiciiModel


# Create your views here.

class ServiciiDetailView(DetailView):
    template_name = "servicii/../templates/detalii.html"
    model = ServiciiModel # Select * from ServiciiModel where id=pk


class ServiciiListView(ListView):
    template_name = "servicii/all.html"
    model = ServiciiModel





class ServiciiUpdateView(UpdateView):
    form_class = ServiciiForm
    template_name = "create_update_form.html"
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')

class ServiciiDeleteView(DeleteView):
    template_name = "delete_form.html"
    model = ServiciiModel
    success_message = "Serviciu sters cu succes"
    success_url = reverse_lazy('serviciu-all')

class ServiciiCreateView(CreateView):
        form_class = ServiciiForm
        template_name = "create_update_form.html"
        model = ServiciiModel
        success_url = reverse_lazy('serviciu-all')

