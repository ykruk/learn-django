from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^exposition/(?P<pk>\d+)/$', views.exposition_detail, name='exposition_detail'),
    url(r'^news', views.news, name='new'),
    url(r'^feedback', views.feedback, name='feedback'),
    url(r'post/new/', views.post_new, name='post_new'),
    # url(r'post/edit/', views.post_edit, name='post_edit'),
] 