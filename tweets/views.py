from django.shortcuts import get_object_or_404, render
from .models import Tweet
from django.http import HttpResponse, Http404, HttpRequest, JsonResponse
from .forms import TweetForm
from random import randint


# current : 2:37:11 - Handling form errors

def home(request):
    tweets = Tweet.objects.all().order_by('-pk')
    form = TweetForm(request.POST or None)

    if request.is_ajax():
        print("AJAXAJAXAJAXAJAXAJAXAJAX")
        if request.method == 'POST':
            print("POST POST")
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                # content = request.POST.get('content')
                data = {"message": "Tweet created!", "tweet": obj.content, "pk": obj.pk, "likes": obj.rand_likes()}
                return JsonResponse(data, status=201)
            else:
                data = {"message": "Error occured while submitting form, check if its valid!"}
                return JsonResponse(data, status=400)

    return render(request, 'pages/home.html', {"tweets": tweets, 'form': form})


def tweete_create_view(request):
    form = TweetForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm

    return render(request, 'pages/home.html', context={'form': form})


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
