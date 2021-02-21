from django.db import models
from django.contrib.auth.models import User
from apps.links.models import Link

class Comment(models.Model):
    body = models.TextField(max_length=1000)
    commented_to = models.ForeignKey(Link, on_delete=models.CASCADE,related_name='comments')
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    commented_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"Comment on {self.commented_to}"