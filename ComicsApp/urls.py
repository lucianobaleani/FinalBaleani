from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("autores/", AuthorList.as_view(), name="author_list"),
    path("autores/crear/", AuthorCreation.as_view(), name="author_creation"),
    path("autores/eliminar/<pk>", AuthorDelete.as_view(), name="author_delete"),
    path("autores/editar/<pk>", AuthorUpdate.as_view(), name="author_update"),
    # path("editorials/", views.EditorialList),
    # path("comics/", views.ComicList.as_view()),
]
