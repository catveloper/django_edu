from django.db import models

# Create your models here.
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('별칭', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('설명', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('내용')
    tags = TaggableManager(blank=True)
    created_dt = models.DateTimeField('작성일', auto_now_add=True)
    modify_dt = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_post'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
