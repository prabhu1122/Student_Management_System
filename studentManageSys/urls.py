
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, staff_views, students_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name = "base"),
    #login
    path('', views.LOGIN, name = "login"),
    path('doLogin', views.doLogin, name= "doLogin"),
    path('register', views.REGISTER, name = "register"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
