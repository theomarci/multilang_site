from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import blog_article

# Create your views here.
# I create now a view to display on my machine the list of the different article saved in my database.

def articleList(request) :
    article = blog_article.objects.all().values()
    template = loader.get_template('main.html')
    context = {
        'article' : article,
    }
    return HttpResponse(template.render(context, request))

