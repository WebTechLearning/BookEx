from django.db import models


class book(object):
	title = models.CharField(max_length=20)

 	"""docstring for book"""
 	def __unicode__(self):
 		return self.title
# Create your models here.
