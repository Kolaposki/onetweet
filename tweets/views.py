from django.shortcuts import get_object_or_404, render
from .models import Tweet
from django.http import HttpResponse, Http404, HttpRequest, JsonResponse


# Create your views here.

def tweet_detail_view(request, pk):
    tweet_obj = get_object_or_404(Tweet, pk=pk)
    data = {}
    if tweet_obj:
        data['message'] = "Success"
        data['text'] = tweet_obj.text
        data['pk'] = tweet_obj.pk

    return JsonResponse(data)
