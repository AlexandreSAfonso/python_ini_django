from django.shortcuts import render, redirect
from phone import models

# Create your views here.
def index(request):
    if request.method == 'POST':
        func = models.Func.create_func(
            phone_number = request.POST['phone_number'],
            alias = request.POST['alias']
        )
        context = []
        if func is not None:
            func.save()
            context ={
                'phone_number':request.POST['phone_number'],
                'alias':request.POST['alias']
            }
        else:
            context ={
                'error': 'Funcionário não Criado. Tente Novamten :('
            }
    return render(request, 'index.html')

def registered_func(request): 
    all_func = models.Func.objects.all()
    context={
        'all_func':all_func
    }
    return render(request, 'registered-func.html', context)

def edit_func(request, phone_number):
    func = models.Func.objects.get(phone_number=phone_number)
    if request.method == 'POST':
        func.phone_number = request.POST['phone_number']
        func.alias = request.POST['alias']
        func.save()
        return redirect('registered_func')
    return render(request, 'edit-func.html',{
        'func':func
    })
