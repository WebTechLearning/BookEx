from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    paperback = models.CharField(max_length=5)
    publisher = models.CharField(max_length=64)
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)
    create_date = models.DateField()
    publish_date = models.DateField()
    comment = models.TextField(blank=True)
    cover = models.ImageField(upload_to='image', blank=True)
    
    """docstring for book"""
    def __unicode__(self):
        return self.title