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


class AuthorUpdate(UpdateView):
    model = Author
    success_url = reverse_lazy("author_list")
    fields = ["name", "role", "currently_active"]


# VISTAS DE EDITORIAL
class EditorialList(ListView):
    model = Editorial
    template_name = "ComicsApp/editorial_list.html"


class EditorialCreation(CreateView):
    model = Editorial
    success_url = reverse_lazy("editorial_list")
    fields = ["name", "country", "state"]


class EditorialDelete(DeleteView):
    model = Editorial
    success_url = reverse_lazy("editorial_list")


class EditorialUpdate(UpdateView):
    model = Editorial
    success_url = reverse_lazy("editorial_list")
    fields = ["name", "country", "state"]


# VISTAS DE COMIC
class ComicList(ListView):
    model = Comic
    template_name = "ComicsApp/comic_list.html"


class ComicCreation(CreateView):
    model = Comic
    success_url = reverse_lazy("comic_list")
    fields = ["name", "editorial", "author", "published_year"]


class ComicDelete(DeleteView):
    model = Comic
    success_url = reverse_lazy("comic_list")


class ComicUpdate(UpdateView):
    model = Comic
    success_url = reverse_lazy("comic_list")
    fields = ["editorial", "name", "author", "published_year"]
