from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampMixin):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.title



class Post(TimeStampMixin):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to="/posts/")
    content = HTMLField()



    def __str__(self):
        return self.title
