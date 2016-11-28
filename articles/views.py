from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.utils import ProgrammingError
import logging


from .models import Content,Metadata,LongArticle


def index(request):
    try:
        latest_post_list = Content.objects.order_by('-article_date')[:5]
        carousel = Content.objects.order_by('-article_date')[:3]
        older_post_list = Content.objects.order_by('-article_date')[:10]
        context = {'latest_post_list': latest_post_list, 'carousel':carousel,'older_post_list':older_post_list }
    except ProgrammingError as e:
 +        logger.warning('Some migrations are not applied!')

    return render(request, 'articles/new/index03.html', context)

def article(request, article_name_slug):

    context_dict = {}
    latest_post_list = Content.objects.order_by('-article_date')[:5]
    older_post_list = Content.objects.order_by('-article_date')[:4:9]



    article = Content.objects.get(slug=article_name_slug)
    context_dict = {'article': article, 'latest_post_list': latest_post_list}

  
    return render(request, 'articles/new/blog-post.html', context_dict)

