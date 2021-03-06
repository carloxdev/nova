# Django's Libraries
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Decoradores
from django.contrib.auth.decorators import login_required
from home.decorators import group_required
from django.utils.decorators import method_decorator

from django.views.generic.base import View

from django.db.models import Q

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Own's Libraries
from .models import Post
from .forms import PostForm

from ebs.business import EmpleadoBusiness
from datetime import datetime


class PostPublicados(View):

    def __init__(self):
        self.template_name = 'inicio.html'

    def get(self, request):

        query = request.GET.get('q')
        if query:
            registros = Post.objects.filter(
                Q(titulo__icontains=query) |
                Q(contenido__icontains=query)
            ).order_by("-created_date")
        else:
            registros = Post.objects.filter(
                status="PUB").order_by("-created_date")
        ultimos = Post.objects.filter(
            status="PUB").order_by("-created_date")[:5]
        lista_cumpleanios = self.lista_fecha_cumpleanios()
        print lista_cumpleanios.sort()

        paginador = Paginator(registros, 10)
        pagina = request.GET.get('page')

        try:
            posts = paginador.page(pagina)
        except PageNotAnInteger:
            posts = paginador.page(1)
        except EmptyPage:
            posts = paginador.page(paginador.num_page)

        contexto = {
            'registros': posts,
            'ultimos': ultimos,
            'lista_cumpleanios': lista_cumpleanios,
            'clave': 'publicados',
        }

        return render(request, self.template_name, contexto)

    def lista_fecha_cumpleanios(self):
        hoy = datetime.now()
        empleado = EmpleadoBusiness.get_Activos()
        e = []
        incluir = {}

        for dato in empleado:
            f = dato.pers_fecha_nacimiento.split(" ")
            if f[0] != "-":
                fecha_nacimiento = datetime.strptime(f[0], '%Y-%m-%d').date()
                if fecha_nacimiento.month == hoy.month:
                    if fecha_nacimiento.day >= hoy.day:
                        incluir = {}
                        incluir['dia'] = fecha_nacimiento.day
                        incluir['nombre'] = dato.pers_nombre_completo
                        e.append(incluir)
        return e


class PostConsultar(View):

    def __init__(self):
        self.template_name = 'post/post_view.html'

    def get(self, request, pk):

        post = get_object_or_404(Post, pk=pk)
        registros = Post.objects.filter(
            status="PUB").exclude(pk=pk).order_by("-created_date")[:5]

        contexto = {
            'registro': post,
            'registros': registros,
            'clave': 'post',
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('MARKETING_ADMIN'), name='dispatch')
class PostAdministracion(View):

    def __init__(self):
        self.template_name = 'post/post_administracion.html'

    def get(self, request):

        query = request.GET.get('q')
        if query:
            registros = Post.objects.filter(
                Q(titulo__icontains=query) |
                Q(contenido__icontains=query)
            ).order_by("-created_date")
        else:
            registros = Post.objects.all().order_by("-created_date")

        paginador = Paginator(registros, 10)
        pagina = request.GET.get('page')

        try:
            posts = paginador.page(pagina)
        except PageNotAnInteger:
            posts = paginador.page(1)
        except EmptyPage:
            posts = paginador.page(paginador.num_page)

        contexto = {
            'registros': posts,
            'clave': 'administracion',
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('MARKETING_ADMIN'), name='dispatch')
class PostNuevo(View):

    def __init__(self):
        self.template_name = 'post/post_form.html'
        self.operation = "Nuevo"

    def get(self, request):

        formulario = PostForm()
        contexto = {
            'form': formulario,
            'operacion': self.operation
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = PostForm(request.POST, request.FILES)

        if formulario.is_valid():
            post = formulario.save(commit=False)

            post.created_by = request.user.profile
            post.updated_by = request.user.profile

            post.save()

            return redirect(reverse('editorial:post_administracion'))

        contexto = {
            'form': formulario,
            'operacion': self.operation
        }
        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('MARKETING_ADMIN'), name='dispatch')
class PostEditar(View):

    def __init__(self):
        self.template_name = 'post/post_form.html'
        self.operation = "Editar"

    def get(self, request, pk, clave):

        post = get_object_or_404(Post, pk=pk)

        formulario = PostForm(
            instance=post
        )

        contexto = {
            'form': formulario,
            'clave': clave,
            'operacion': self.operation
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk, clave):
        post = get_object_or_404(Post, pk=pk)

        formulario = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if formulario.is_valid():

            post = formulario.save(commit=False)
            post.updated_by = request.user.profile

            post.save()

            if clave == 'administracion':
                return redirect(reverse('editorial:post_administracion'))
            elif clave == 'publicados':
                return redirect(reverse('home:inicio'))
            elif clave == 'post':
                return redirect(reverse('editorial:post_consultar', kwargs={'pk': post.pk}))

        contexto = {
            'form': formulario,
            'operacion': self.operation
        }
        return render(request, self.template_name, contexto)
