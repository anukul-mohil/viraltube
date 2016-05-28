import requests

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from feeds import CATEGORY_MAP

def index(request):
    """
    Index page for the project
    """
    API_KEY='dummy'
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&key=%s&part=snippet&maxResults=10' % API_KEY)
    json_body = response.json()
    regions = ['UK', 'US', 'IN']
    context = {'regions': regions, 'categories': CATEGORY_MAP.keys()}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
