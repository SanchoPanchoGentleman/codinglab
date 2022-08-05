"""watersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from watersite import settings
from filter.views import *
from django.urls import path, include


urlpatterns = [
    path('captcha/', include('captcha.urls')),  # Captcha connection
    path('admin/', admin.site.urls),
    path('', include('filter.urls')),  # http://127.0.0.1:8000, # include('filter.urls') нужен для того чтобы

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound   # в случае если страница не найдена и DEBUG=False в файле settings.py тогда будет
# показывать что страница не найдена

