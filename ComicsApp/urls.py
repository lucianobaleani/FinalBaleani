from django.urls import path

# from django import views
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    # INICIO
    path("", home, name="home"),
    # LOGIN
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("editar_perfil/", edit_profile, name="edit_profile"),
    path("agregar_avatar/", add_avatar, name="add_avatar"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # COMICS
    path("comics/", ComicList.as_view(), name="comic_list"),
    path("comics/crear/", ComicCreation.as_view(), name="comic_creation"),
    path("comics/eliminar/<pk>", ComicDelete.as_view(), name="comic_delete"),
    path("comics/editar/<pk>", ComicUpdate.as_view(), name="comic_update"),
    path("comics/list", ComicDetailView.as_view(), name="comic_detail_list"),
    path("agregarPortada/", add_cover, name="add_cover"),
    # ACERCA DE MI
    path("acerca_de_mi/", about_me, name="about_me"),
]
