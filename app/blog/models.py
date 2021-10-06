from django.db import models


# Create your models here.

class blog(models.Model):
    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('제목별칭', max_length=50)
    description = models.CharField('내용 한줄 설명', max_length=100)
    content = models.TextField('내용')
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
