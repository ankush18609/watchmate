from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import datetime

class movie(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=300)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class streamplateform(models.Model):
    name = models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    def __str__(self):
        return self.name
class watchlist(models.Model):
    title=models.CharField(max_length=30)
    storyline=models.CharField(max_length=150)
    streaming_plateform=models.ForeignKey(streamplateform,on_delete=models.CASCADE,related_name='watchlist')
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title
class review(models.Model):
    movie=models.ForeignKey(watchlist, on_delete=models.CASCADE,related_name='reviews')
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.rating)+"|"+str(self.description)


