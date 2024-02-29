from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from users.forms import UserForm
from users.models import UsersModel


# CRUD

# CREATE
class CreateUserView(CreateView):
    model = UsersModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')


# READ
class UsersListView(ListView):
    model = UsersModel
    template_name = 'users/all.html'


# Update
class UsersUpdateView(UpdateView):
    model = UsersModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')


# DELETE
class UsersDeleteView(DeleteView):
    model = UsersModel
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users-all')


class UserDetailView(DetailView):
    model = UsersModel
    template_name = 'users/detalii.html'