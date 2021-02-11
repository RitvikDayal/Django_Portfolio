from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def contact(request):
    return render(request, 'portfolio/contact.html')