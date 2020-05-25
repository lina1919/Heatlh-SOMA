from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(default=timezone.now)
    body=models.TextField(default='')
    objects = models.Manager()
    image = models.ImageField(upload_to='images/',blank=True)
    file = models.FileField(upload_to='documents/%Y.%m',blank=True)
    #파일 저장 위치가 document/(년,월)폴더로 설정됨.
class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)