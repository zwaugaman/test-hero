from django.conf.urls import url

from . import views

urlpatterns = [
    # ex" /pdf/
    url(r'^generate/$', views.some_view, name='generate'),

    # ex: /pdf/button/
    url(r'^button/$', views.button_view.as_view(), name='button'),

]