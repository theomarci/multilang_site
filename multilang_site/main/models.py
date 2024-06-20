from django.db import models

# Create your models here.
# I create a model with 3 differents attributes : title, content and publication_date.

class blog_article(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=6000)
    publication_date = models.DateField()