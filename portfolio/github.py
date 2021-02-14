import requests

def get_repos():
    response = requests.get('https://api.github.com/users/ritvikdayal/repos?per_page=100&sort=created')
    return response.json()

def filter_repo(repo):
    data = {
        'name': repo['name'],
        'url': repo['html_url'],
        'description': repo['description'],
        'stars': repo['stargazers_count'],
        'created': repo['created_at'],
    }

    return data

