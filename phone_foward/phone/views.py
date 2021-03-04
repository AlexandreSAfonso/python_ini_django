from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        context ={
            'phone_number':request.POST['phone_number'],
            'alias':request.POST['alias']
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')