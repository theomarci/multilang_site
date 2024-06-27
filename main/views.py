from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import blog_article

# Create your views here.
# I create now a view to display on my machine the list of the different article saved in my database.

def articleList(request) :
    # Fetch all articles from the BlogArticle model and return them as dictionaries
    article = blog_article.objects.all().values()
    # Load the template 'main.html'
    template = loader.get_template('main.html')
    # Define the context dictionary to pass data to the template
    context = {
        'article' : article,
    }
     # Render the template with the given context and return an HttpResponse
    return HttpResponse(template.render(context, request))

