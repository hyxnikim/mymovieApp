from django.db import models
from django.utils.functional import cached_property

class Movie(models.Model):
    no = models.IntegerField(primary_key=True)
    title = models.CharField(max_length =100)
    src = models.TextField(default="")
    synp = models.TextField(default="")
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie,related_name='reviews')
    contents = models.TextField(default="")
    sentiments = models.TextField(default="")
    sentiments_neg = models.FloatField(null=True, blank=True, default=None)
    sentiments_pos = models.FloatField(null=True, blank=True, default=None)
    sentiments_neu = models.FloatField(null=True, blank=True, default=None)
    sentiments_comp = models.FloatField(null=True, blank=True, default=None)
