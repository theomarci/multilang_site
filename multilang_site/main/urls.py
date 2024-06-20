from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views

# here I write my root

urlpatterns = [
    path('', views.articleList, name='articleList'),
]

