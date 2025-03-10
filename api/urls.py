from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('get_all_report', views.get_all_report),
    path('create_report', views.create_report),
    path('add_form', views.add_form),      
    path('add_sec', views.add_section),
    path('add_image', views.add_image),
    path('dowload_select_report', views.dowload_select_report),
    path('get_select_report', views.get_select_report),
    path('update_select_report', views.update_select_report),
    path('delete_report', views.delete_report),
    #path('check_miss_spell', views.check_miss_spell),
    path('register', views.register_user),
    path('login', views.login),
    path('get_all_user',views.get_all_user),
    path('delete_user',views.delete_user),
    path('user_update_role',views.user_update_role),
    path('get_all_format',views.get_all_format),
    path('dowload_select_format',views.dowload_select_format),
    path('update_format',views.update_format),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
