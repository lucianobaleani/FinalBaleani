from django.shortcuts import render
from .models import Comic, Author, Editorial
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# INICIO
def home(request):
    return render(request, "ComicsApp/home.html")


# VISTAS DE AUTOR
class AuthorList(ListView):
    model = Author
    template_name = "ComicsApp/author_list.html"


class AuthorCreation(CreateView):
    model = Author
    success_url = reverse_lazy("author_list")
    fields = ["name", "role", "currently_active"]


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy("author_list")


class AuthorUpdate(UpdateView):  # vista usada para EDITAR
    model = Author
    success_url = reverse_lazy("author_list")
    fields = ["name", "role", "currently_active"]


# class EditorialList(ListView):
#     model = Editorial


# class ComicList(ListView):
#     model = Comic
#     template_name = "ComicsApp/"
