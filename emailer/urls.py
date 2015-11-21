from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ emailer }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^cat/', include('cat.urls')),
    url(r'^pdf/', include('pdf_generator.urls', namespace="generator")),
)
