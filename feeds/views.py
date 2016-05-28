import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from feeds import API_KEY, CATEGORY_MAP

# tags:[video_id]
tags_map = {}

#Todo: wire this with redis
def generate_tags(json_body):
    """
    constructs a {tag:[video_id]} dict
    """
    for video in json_body['items']:
        try:
            for tag in video['snippet']['tags']:
                if tag not in tags_map:
                    tags_map[tag] = [video['id']]
                else:
                    tags_map[tag].append([video['id']])
        except KeyError:
            print "tags doesnt exist for this video ", video['id']

def index(request):
    """
    Index page for the `feeds` application
    """
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&key=%s&part=snippet&maxResults=10' % API_KEY)
    json_body = response.json()
    regions = ['UK', 'US', 'IN']
    context = {'regions': regions, 'categories': CATEGORY_MAP.keys()}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def music(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['music'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    print tags_map
    template = loader.get_template('feeds/categories.html')
    # return HttpResponse(template.render(context, request))
    return HttpResponse(json_body['items'], content_type='application/json')

def sports(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['sports'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    return HttpResponse(json_body['items'], content_type='application/json')

def travel_events(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['travel_events'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def gaming(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['gaming'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def comedy(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['comedy'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def entertainment(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['entertainment'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def news_politics(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['news_politics'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def education(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['education'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def science_technology(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['science_technology'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def movies(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['movies'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def animation(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['animation'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def action_adventure(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['action_adventure'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')

def trailers(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&regionCode=US&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['trailers'], API_KEY))
    json_body = response.json()
    generate_tags(json_body)
    context = {'response': json_body}
    template = loader.get_template('feeds/categories.html')
    return HttpResponse(json_body['items'], content_type='application/json')
