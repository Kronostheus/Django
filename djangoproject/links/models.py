from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Link(models.Model):
    title = models.CharField("Headline", max_length=100)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rank = models.FloatField(default = 0.0)
    url = models.URLField("URL", max_length=250, blank=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("link_detail", kwargs={"pk": str(self.id)})

    def __str__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return "%s upvoted %s" % (self.voter.username, self.link.title)

class Comment(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='comments')
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text

