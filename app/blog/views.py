from django.shortcuts import render

# Create your views here.
from django.views.generic import *

from app.blog.models import Post


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostAV(ArchiveIndexView):
    model = Post
    template_name = 'blog/post_archive.html'
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    template_name = 'blog/post_archive_year.html'
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    template_name = 'blog/post_archive_month.html'
    date_field = 'modify_dt'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Post
    template_name = 'blog/post_archive_day.html'
    date_field = 'modify_dt'
    month_format = '%m'


class PostTAV(TodayArchiveView):
    model = Post
    template_name = 'blog/post_archive_day.html'
    date_field = 'modify_dt'
    month_format = '%m'
