from django.shortcuts import get_object_or_404, render
from .models import Tweet
from django.http import HttpResponse, Http404, HttpRequest, JsonResponse


def home(request):
    return render(request, 'pages/home.html')


def tweet_list_view(request):
    """
    View to get all tweets
    :param request:
    :return: JSON object
    """

    qs = Tweet.objects.all()
    all_tweets = [{"pk": tweet.pk, "content": tweet.content} for tweet in qs]
    data = {"tweets": all_tweets}
    return JsonResponse(data)


def tweet_detail_view(request, pk):
    tweet_obj = get_object_or_404(Tweet, pk=pk)
    data = {}
    if tweet_obj:
        data['message'] = "Success"
        data['content'] = tweet_obj.content
        data['pk'] = tweet_obj.pk

    return JsonResponse(data)
