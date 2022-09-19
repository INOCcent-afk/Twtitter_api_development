from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TweetSerializer
from .models import Tweet
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def AllTweetsView(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)

    return Response(serializer.data)
