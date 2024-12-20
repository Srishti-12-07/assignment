from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import AuthenticationForm

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Dashboard view (authenticated users only)
@login_required
def dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'employees': employees})

# Add employee view
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

# Edit employee view
@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})
