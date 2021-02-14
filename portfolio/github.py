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
        'created': repo['created_at']
    }

    return data

def add_image(repos):

    images = [
        'covidtweetsanalysis.png',
        'supportportal.png',
        'thestoneshop.png',
        'facerecognition.jpg',
        'clickbait.jpg',
        'Cdrgen.png',
        'movierecommendation.jpeg',
        'algorithms.png',
    ]

    for image, repo in zip(images, repos):
        repo['image_file'] = 'portfolio/images/Projects/'+image,
    
    return repos
    
