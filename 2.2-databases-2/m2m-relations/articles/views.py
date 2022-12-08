from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    article_objects = Article.objects.all()
    context = {'object_list': article_objects}

    return render(request, template, context)
