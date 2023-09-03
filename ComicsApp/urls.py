from django.urls import path
from .views import *


urlpatterns = [
    # INICIO
    path("", home, name="home"),
    # AUTORES
    path("autores/", AuthorList.as_view(), name="author_list"),
    path("autores/crear/", AuthorCreation.as_view(), name="author_creation"),
    path("autores/eliminar/<pk>", AuthorDelete.as_view(), name="author_delete"),
    path("autores/editar/<pk>", AuthorUpdate.as_view(), name="author_update"),
    # EDITORIALES
    path("editoriales/", EditorialList.as_view(), name="editorial_list"),
    path("editoriales/crear/", EditorialCreation.as_view(), name="editorial_creation"),
    path(
        "editoriales/eliminar/<pk>", EditorialDelete.as_view(), name="editorial_delete"
    ),
    path("editoriales/editar/<pk>", EditorialUpdate.as_view(), name="editorial_update"),
    # COMICS
    path("comics/", ComicList.as_view(), name="comic_list"),
    path("comics/crear/", ComicCreation.as_view(), name="comic_creation"),
    path("comics/eliminar/<pk>", ComicDelete.as_view(), name="comic_delete"),
    path("comics/editar/<pk>", ComicUpdate.as_view(), name="comic_update"),
]
