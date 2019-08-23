from django.db import models

# Create your models here.
class MemoAppModel(models.Model):
    title = models.CharField(max_length=50, blank=True)#제목
    nickname = models.CharField(max_length=50, blank=True)#ID
    create_date = models.DateField(null=True, blank=True)#등록일
    memo = models.CharField(max_length=200, blank=True)#내용
    hits = models.IntegerField(null=True, blank=True)#조회수