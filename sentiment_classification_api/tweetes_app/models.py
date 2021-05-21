from django.db import models
# Tweet model
class Tweet(models.Model):
	#sentiments
	SENTIMENTS = (
        ('POS', 'Postive'),
        ('NUE', 'Negative'),
        ('NEG', 'Neutral'),
    )

	unique_id = models.TextField()
	#content of the tweet 
	content = models.TextField()
	#sentiment for the tweet 
	sentiment = models.CharField(max_length=3, choices=SENTIMENTS,blank=True)

