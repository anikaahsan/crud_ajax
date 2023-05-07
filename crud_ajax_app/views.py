from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def list(request):
    employees=Employee.objects.all()
    context=dict(employees=employees)
    return render(request,'employee_list.html',context)


def employee_create(request):

    data=dict()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            employees=Employee.objects.all()
            context=dict(employees=employees)
            data['form_is_valid']=True
            data['html_employee_list']=render_to_string('partial_employee_list.html',context)      
        else:
            data['form_is_valid']=False 
       
    else:
        form=EmployeeForm()

    context=dict(form=form)
    html_form=render_to_string('partial_employee_create.html',context,request=request)
    data['html_form']=html_form
    return JsonResponse(data)


def employee_update(request,pk):
    employee=Employee.objects.get(pk=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
    else:
        form=EmployeeForm(instance=employee)

    return save_employee_form(request,form,'partial_employee_update.html')



def save_employee_form(request,form,template_name):
    data=dict()
    if request.method=='POST':
        if form.is_valid():
            form.save()
            data['form_is_valid']=True
            employees=Employee.objects.all()
            context=dict(employees=employees)
            data['html_employee_list']=render_to_string('partial_employee_list.html',context)
        
        else:
            data['form_is_valid']=False

    context=dict(form=form)
    data['html_form']=render_to_string(template_name,context,request=request)
    return JsonResponse(data)    
                 






def delete(request,pk):
    data=dict()
    employee=Employee.objects.get(pk=pk)
    if request.method=="POST":
        employee.delete()
        data['form_is_valid']=True
        employees=Employee.objects.all()
        context=dict(employees=employees)
        data['html_employee_list']=render_to_string('partial_employee_list.html',context)
    
    else:
        context=dict(employee=employee)
        data['html_form'] = render_to_string('partial_employee_delete.html',
            context,
            request=request,
        )

    return JsonResponse(data)    
