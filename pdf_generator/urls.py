from django.conf.urls import url

from . import views

urlpatterns = [
    # ex" /pdf/
    url(r'^$', views.some_view, name='index'),

]