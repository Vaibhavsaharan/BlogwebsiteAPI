from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    postuuid = models.CharField(primary_key=True, max_length=70, blank=False, default=uuid.uuid4)
    title = models.CharField(max_length=70, blank=False)
    username = models.CharField(max_length=70, blank=False)
    published_on = models.DateTimeField(auto_now = True)
    content = models.JSONField()



