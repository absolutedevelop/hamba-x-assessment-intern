from django.urls import include, path
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'tweets', views.TweetViewSet)
#path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

urlpatterns = [
	path('tweet/', views.TweetsList, name='tweet-list'),
	path('tweet/<str:uid>/', views.SingleTweet, name='tweet-single'),

	path('create/tweet/', views.CreateTweet, name='new-tweet'),
	path('update/tweet/<str:uid>/', views.UpdateTweet, name='update-tweet'),
	path('delete/<str:uid>/', views.DeleteTweet, name='delete-tweet'),

]