from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:id>/', views.edit_employee, name='edit_employee'),
]
