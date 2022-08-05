import kwargs as kwargs
import self as self
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import *
from .models import *
from .utils import *

# DataMixin это класс который обьединяет общие параметры значения и помогает сократить повторяющийся код
class FilterHome(DataMixin, ListView): # класс представления страницы заменяет строчки кода с def index(request)

    model = Filter
    template_name = 'filter/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")    # c_def <- эта строка вызывает код с util.py в котором написан контекст
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Filter.objects.filter(is_published=True)

# def index(request):
#     posts = Filter.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'filter/index.html', context=context)

def about(request):
    return render(request, 'filter/about.html', {'menu': menu, 'title': 'О сайте'})


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#           #  print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'filter/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'filter/addpage.html'
    login_url = reverse_lazy('home')
    raise_exception = True

    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Adding post")  # c_def <- эта строка вызывает код с util.py в котором написан контекст
        return dict(list(context.items()) + list(c_def.items()))




# def contact(request):
#     return HttpResponse("Обратная связь")

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'filter/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def =  self.get_user_context(title="Feedback")  # c_def <- эта строка вызывает код с util.py в котором написан контекст
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def show_post(request, post_slug):
#     post = get_object_or_404(Filter, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'filter/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Filter
    template_name = 'filter/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])  # c_def <- эта строка вызывает код с util.py в котором написан контекст
        return dict(list(context.items()) + list(c_def.items()))

class FilterCategory(DataMixin, ListView):  # класс представления страницы заменяет строчки кода с def index(request)

    model = Filter
    template_name = 'filter/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Filter.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat))  # c_def <- эта строка вызывает код с util.py в котором написан контекст
        cat_selected = context['posts'][0].cat_id
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_id):
#     posts = Filter.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Category show',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'filter/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'filter/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")  # c_def <- эта строка вызывает код с util.py в котором написан контекст
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'filter/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")  # c_def <- эта строка вызывает код с util.py в котором написан контекст
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('home') ## при удачной авторизации, пользователя переносит на главную страницу

def logout_user(request):
    logout(request)
    return redirect('login')