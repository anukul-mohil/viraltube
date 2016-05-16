import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from feeds import API_KEY, CATEGORY_MAP


def index(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&key=%s&part=snippet&maxResults=10' % API_KEY)
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def music(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['music'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def sports(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['sports'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def travel_events(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['travel_events'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def gaming(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['gaming'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def comedy(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['comedy'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def entertainment(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['entertainment'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def news_politics(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['news_politics'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def education(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['education'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def science_technology(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['science_technology'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def movies(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['movies'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def animation(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['animation'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def action_adventure(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['action_adventure'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

def trailers(request):
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&regionCode=US&videoCategoryId=%s&key=%s&part=snippet&maxResults=10' % (CATEGORY_MAP['trailers'], API_KEY))
    json_body = response.json()
    context = {'response': json_body}
    template = loader.get_template('feeds/index.html')
    return HttpResponse(template.render(context, request))

