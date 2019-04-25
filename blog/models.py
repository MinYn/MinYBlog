from django.db import models
from common.util.utils import user_path


class bloglist(models.Model):
    Title = models.CharField(max_length=30000, verbose_name="제목")
    SubTitle = models.CharField(max_length=200, verbose_name="부제목")
    Subject = models.TextField(default='', verbose_name="내용")
    picture = models.ImageField(upload_to=user_path, blank=True, verbose_name="배경사진")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="추가날짜")