from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_employee/', views.add_employee_view, name='add_employee'),
    path('employee_list/', views.employee_list_view, name='employee_list'),
    path('edit_employee/<int:employee_id>/', views.edit_employee_view, name='edit_employee'),
]
