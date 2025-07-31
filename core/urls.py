from django.urls import path
from .views import  admin_view, admin_login, add_student_view

urlpatterns = [
    path('admin-page/', admin_view, name='admin-page'),
    path('admin-login/', admin_login, name='admin-login'),
    path('add-student/', add_student_view, name='add-student'),
]