from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TweetSerializer
from .models import Tweet

import uuid

  



#class TweetViewSet(viewsets.ModelViewSet):
#   queryset = Tweet.objects.all()
#    serializer_class = TweetSerializer

#get a list of tweets
@api_view(['GET'])
def TweetsList(request):
	
	tweets = Tweet.objects.all()
	serializer  = TweetSerializer(tweets,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def SingleTweet(request,uid):
	
	tweets = Tweet.objects.get(unique_id=uid)
	serializer  = TweetSerializer(tweets)
	return Response(serializer.data)


@api_view(['POST'])
def CreateTweet(request):
	data = request.data 
	data["unique_id"] = str(uuid.uuid1())
	serializer = TweetSerializer(data=data)

	if serializer.is_valid():
		serializer.save()
	else:
		print("not valid")

	return Response(serializer.data)



@api_view(['POST'])
def UpdateTweet(request,uid):
	tweet = Tweet.objects.get(unique_id=uid)	
	serializer = TweetSerializer(instance = tweet, data =request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTweet(request,uid):
	tweet = Tweet.objects.get(unique_id=uid)	
	tweet.delete()

	return Response("Deleted")
