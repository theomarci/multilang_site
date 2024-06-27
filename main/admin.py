from django.contrib import admin
from .models import blog_article

# Register your models here.
# If I want to see my database in the admin page I need to add this single line :

admin.site.register(blog_article)
