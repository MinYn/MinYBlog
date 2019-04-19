from django.db import models
from common.util.utils import user_path
# Create your models here.


class bloglist(models.Model):
    Title = models.CharField(max_length=30000)
    SubTitle = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=user_path, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)