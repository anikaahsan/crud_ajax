from django.urls import path
from . import views

urlpatterns=[
    path('',views.list ,name='list'),
    path('create/',views.employee_create, name='create'),
    path('edit/<int:pk>',views.employee_update ,name='employee_update'),
    path('delete/<int:pk>',views.delete ,name='delete')

    
]