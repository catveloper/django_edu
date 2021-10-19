from django.urls import path, re_path

from app.blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<int:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
    path('archive/tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('archive/tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]
