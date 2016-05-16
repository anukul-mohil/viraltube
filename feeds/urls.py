from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^music$', views.music, name='music'),
            url(r'^sports$', views.sports, name='sports'),
            url(r'^travel_events$', views.travel_events, name='travel_events'),
            url(r'^gaming$', views.gaming, name='gaming'),
            url(r'^comedy$', views.comedy, name='comedy'),
            url(r'^entertainment$', views.entertainment, name='entertainment'),
            url(r'^news_politics$', views.news_politics, name='news_politics'),
            url(r'^education$', views.education, name='education'),
            url(r'^science_technology$', views.science_technology, name='science_technology'),
            url(r'^movies$', views.movies, name='movies'),
            url(r'^animation$', views.animation, name='animation'),
            url(r'^action_adventure$', views.action_adventure, name='action_adventure'),
            url(r'^trailers$', views.trailers, name='trailers'),
            ]
