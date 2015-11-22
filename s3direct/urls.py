from django.conf.urls import patterns, url
from s3direct.views import get_upload_params, button_view, generate_view

urlpatterns = patterns('',
                       url('get_upload_params/',
                           get_upload_params, name='s3direct'),

    # ex: /pdf/button/
    url(r'^button/$', button_view.as_view(), name='button'),

    # ex" /pdf/
    url(r'^generate/$', generate_view, name='generate'),


                       )
