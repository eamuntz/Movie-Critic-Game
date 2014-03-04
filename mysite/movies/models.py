from django.db import models


# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length = 200)
	year = models.DateTimeField('date released')
	mpaa_rating = models.CharField(max_length = 10)
	critic_score = models.IntegerField()
	synopsis = models.CharField(max_length = 1000)
	poster = models.URLField()
	runtime = models.IntegerField()
	director = models.CharField(max_length = 200)
#uncertain how to handle lists so temporarily disabled:	
#	top_reviews = 
#	abridged_cast = 

