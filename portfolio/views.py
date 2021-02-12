from django.shortcuts import render
from . import github

def home(request):
    repos = github.get_repos()
    git_data = []

    for repo in repos:
        if repo['stargazers_count'] > 0:
            git_data.append(github.filter_repo(repo))
        if len(git_data) == 8:
            break
    
    context ={
        'git_repos' : git_data,
    }

    return render(request, 'portfolio/index.html', context=context)

def about(request):
    return render(request, 'portfolio/about.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def contact(request):
    return render(request, 'portfolio/contact.html')