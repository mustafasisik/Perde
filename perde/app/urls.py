from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('bayi_girisi', views.site_login, name='login'),
    path('bayi_basvurusu', views.register, name='register'),
    path('logout', views.site_logout, name='logout'),
    path('siparis_olustur', views.create_order, name='create_order'),
    path('get_districts', views.get_districts, name='get_districts'),
]