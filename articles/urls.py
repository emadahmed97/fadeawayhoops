from django.conf.urls import include,url

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<article_name_slug>[\w\-]+)/$', views.article, name='articles')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
