from django.shortcuts import render


def home(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')


def projects(request):
    return render(request, 'myapp/projects.html')


def contact(request):
    return render(request, 'myapp/contact.html')