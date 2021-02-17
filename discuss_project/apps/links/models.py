from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    title = models.CharField(max_length=350)
    url = models.URLField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True, editable=False)
    upvotes = models.ManyToManyField(User, related_name='votes')


def __str__(self):
    return self.title

    