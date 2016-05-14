from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the homepage for the project. Please go to `/feeds/` endpoint to see top 10 videos feed")
