from django.shortcuts import render
from .models import Comic, Avatar
from .forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin  # VISTA DE CLASE
from django.contrib.auth.decorators import login_required  # VISTA FUNCION
from django.urls import reverse_lazy


# INICIO
def home(request):
    return render(request, "ComicsApp/home.html", {"avatar": get_avatar(request)})


class LoginRequest(LoginView):
    template_name = "ComicsApp/login.html"
    fields = "__all__"
    redirect_autheticated_user = True
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return reverse_lazy("home")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user_name = info["username"]
            form.save()
            return render(
                request,
                "ComicsApp/home.html",
                {
                    "mensaje": f"Usuario {user_name} creado correctamente",
                    "avatar": get_avatar(request),
                },
            )
        else:
            return render(
                request,
                "ComicsApp/register.html",
                {
                    "form": form,
                    "mensaje": "Datos invalidos",
                    "avatar": get_avatar(request),
                },
            )

    else:
        form = UserRegisterForm()
        return render(
            request,
            "ComicsApp/register.html",
            {"form": form, "avatar": get_avatar(request)},
        )


@login_required
def edit_profile(request):
    user = request.user
    avatar = get_avatar(request)
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.email = info["email"]
            user.password1 = info["password1"]
            user.password2 = info["password2"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()
            return render(
                request,
                "ComicsApp/home.html",
                {
                    "message": f"Usuario {user.username} modificado con exito!!!",
                    "avatar": get_avatar(request),
                },
            )
        else:
            return render(
                request,
                "ComicsApp/edit_profile.html",
                {
                    "form": form,
                    "user": user.username,
                    "message": "Datos invalidos",
                    "avatar": get_avatar(request),
                },
            )
    else:
        form = UserEditForm(instance=user)
        return render(
            request,
            "ComicsApp/edit_profile.html",
            {"form": form, "username": user.username, "avatar": get_avatar(request)},
        )


#  VISTAS DE AVATAR


def get_avatar(request):
    avatars = Avatar.objects.filter(user=request.user.id)

    if len(avatars) != 0:
        return avatars[0].image.url
    else:
        return "/media/avatars/undefined.jpg"


@login_required
def add_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(user=request.user, image=request.FILES["image"])
            previous_avatar = Avatar.objects.filter(user=request.user)
            if len(previous_avatar) > 0:
                previous_avatar[0].delete()
            avatar.save()
            return render(
                request,
                "ComicsApp/home.html",
                {
                    "message": f"Avatar agregado correctamente",
                    "avatar": get_avatar(request),
                },
            )
        else:
            return render(
                request,
                "ComicsApp/add_avatar.html",
                {
                    "form": form,
                    "user": request.user,
                    "message": "Error al agregar el avatar",
                },
            )
    else:
        form = AvatarForm()
        return render(
            request,
            "ComicsApp/add_avatar.html",
            {"form": form, "user": request.user, "avatar": get_avatar(request)},
        )


# VISTAS DE COMIC


class ComicList(ListView, LoginRequiredMixin):
    model = Comic
    template_name = "ComicsApp/comic_list.html"


class ComicDetailView(DetailView, LoginRequiredMixin):
    model = Comic
    success_url = reverse_lazy("comic_list")
    template_name = "ComicsApp/comic_detail_list.html"


class ComicCreation(CreateView, LoginRequiredMixin):
    model = Comic
    success_url = reverse_lazy("comic_list")
    fields = [
        "user",
        "cover_image",
        "name",
        "editorial",
        "author",
        "published_year",
    ]


class ComicDelete(DeleteView, LoginRequiredMixin):
    model = Comic
    success_url = reverse_lazy("comic_list")


class ComicUpdate(UpdateView, LoginRequiredMixin):
    model = Comic
    success_url = reverse_lazy("comic_list")
    fields = ["cover_image", "editorial", "name", "author", "published_year"]


@login_required
def get_cover(request):
    covers = Comic.objects.filter(comic=request.comic.id)
    if len(covers) != 0:
        return covers[1].image.url
    else:
        return "/media/covers/undefined.png"


# COMENTARIOS


class CommentPage(LoginRequiredMixin, CreateView):
    model = ChatBox
    form_class = ChatBoxForm
    template_name = "ComicsApp/comments.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.comment_id = self.kwargs["pk"]
        return super(CommentPage, self).form_valid(form)


# ACERCA DE MI
def about_me(request):
    return render(request, "ComicsApp/about_me.html", {"avatar": get_avatar(request)})
