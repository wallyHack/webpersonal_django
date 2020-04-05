from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Mi Web Personal')
    return render(request, 'core/home.html', {})

def about(request):
    return render(request, 'core/about-me.html', {})

def contact(request):
    return render(request, 'core/contact.html', {})

