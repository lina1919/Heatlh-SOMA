"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import mydiary.views
import accounts.views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mydiary.views.home, name="home"),
    path('new/', mydiary.views.new, name="new"),
    path('detail/<int:pk>', mydiary.views.detail, name="detail"),
    path('edit/<int:index>', mydiary.views.edit, name="edit"),
    path('detail/<int:pk>/delete', mydiary.views.delete, name="delete"),
    path('detail/<int:pk>/comment/<int:comment_pk>/delete/', mydiary.views.delete_comment, name="delete_comment"),
    path('registration/register/', accounts.views.register, name="register"),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/login/',auth_views.LoginView.as_view(),{'template_name':'registration/login.html'}, name="login"),
    path('registration/logged_out/', auth_views.LogoutView.as_view(), {'template_name':'registration/logged_out.html'}, name="logout"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)