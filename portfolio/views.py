from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . import github
from .forms import VisitorContactForm

def home(request):
    repos = github.get_repos()
    git_data = []

    for repo in repos:
        if repo['stargazers_count'] > 0:
            git_data.append(github.filter_repo(repo))
        if len(git_data) == 8:
            break
    
    if request.method == 'POST':
        form = VisitorContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_email()
            messages.success(request, f'Thanks for Reaching out I will be contacting back soon!')
            return redirect('home')
        else:
            messages.warning(request, f'Information entered is incorrect! Please try again.')
    else:
        form = VisitorContactForm()
    
    context ={
        'git_repos' : git_data,
        'form': form,
    }

    return render(request, 'portfolio/index.html', context=context)

def about(request):
    return render(request, 'portfolio/about.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def contact(request):
    return render(request, 'portfolio/contact.html')