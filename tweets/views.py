from django.shortcuts import get_object_or_404, render
from .models import Tweet
from django.http import HttpResponse, Http404, HttpRequest, JsonResponse
from .forms import TweetForm


# current : 2:37:11 - Handling form errors

def home(request):
    return render(request, 'pages/home.html')


def tweete_create_view(request):
    form = TweetForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm

    return render(request, 'components/form.html', context={'form': form})


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
