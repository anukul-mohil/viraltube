import requests
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    API_KEY = os.environ['API_KEY']
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&key=%s&part=snippet&maxResults=10' % API_KEY)
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))
