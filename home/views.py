from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'active_home': 'active',
    }
    return render(request,'home/index.html', context)