from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=50)
	score = models. IntegerField()
	def __unicode__(self):
		return self.name
