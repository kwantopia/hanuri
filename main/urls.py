from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='home_page'),
    url(r'^recent/$', 'recent', name='recent'),
    url(r'^contribute/$', 'contribute', name='contribute'),
    url(r'^contact/$', 'contact', name='contact'),
)
