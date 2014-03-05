from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from scorecard.models import Player
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'scorecard/index.html'
	context_object_name = 'players'

	def get_queryset(self):
		"""return our list of players"""
		return Player.objects.all()
