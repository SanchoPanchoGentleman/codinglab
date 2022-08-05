from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', FilterHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', FilterCategory.as_view(), name='category'),
]

    # http://127.0.0.1:8000/home page/ будет перенаправлять на главную страницу по имени
    # path('cats/<slug:cat>/', categories),   # http://127.0.0.1:8000/cats/1/ будет показывать категории по номерам
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

