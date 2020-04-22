from django.shortcuts import get_object_or_404, render
from .models import Tweet
from django.http import HttpResponse, Http404, HttpRequest, JsonResponse


# Create your views here.

def tweet_detail_view(request):
    return HttpResponse("<h2>Hello World</h2>")
