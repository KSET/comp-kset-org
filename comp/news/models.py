from django.db import models
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

class News(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    author = models.ForeignKey(User)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
