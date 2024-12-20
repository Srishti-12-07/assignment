from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .models import Employee


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        try:
            user = User.objects.get(username=username, password=password)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('dashboard')
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

def add_employee_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        department = request.POST['department']
        salary = request.POST['salary']

        Employee.objects.create(
            name=name,
            designation=designation,
            department=department,
            salary=salary
        )
        messages.success(request, "Employee added successfully!")
        return redirect('employee_list')

    return render(request, 'add_employee.html')

def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def edit_employee_view(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.designation = request.POST['designation']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.save()
        messages.success(request, "Employee details updated successfully!")
        return redirect('employee_list')

    return render(request, 'edit_employee.html', {'employee': employee})