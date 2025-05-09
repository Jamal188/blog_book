"""
URL configuration for blogs_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from blogs import views
from django.views.generic.base import RedirectView as redirect
from django.views.decorators.csrf import ensure_csrf_cookie 
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
@ensure_csrf_cookie
def csrf_token_view(request):
    return JsonResponse({'csrfToken': request.META['CSRF_COOKIE']})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('blogs/', include('blogs.urls')),
    path('welcome', views.welcome_view),
    path('', redirect.as_view(url='welcome')),
    path('home', views.home , name='home'),
    path('load_blogs', views.load_blogs, name='load_blogs'),
    path('csrf-token/', csrf_token_view, name='csrf-token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)