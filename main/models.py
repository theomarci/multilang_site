from django.db import models

# Create your models here.
# I create a model with 3 differents attributes : title, content and publication_date.

class blog_article(models.Model) :
    # title field with the max length
    title = models.CharField(max_length=50)
    # content field with a text area
    content = models.TextField(max_length=6000)
    # date field
    publication_date = models.DateField()