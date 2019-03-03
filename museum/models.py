from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    photo = models.ImageField(upload_to='news', default='news.png')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Exposition(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    add_text = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='exp', default='exp.png')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title