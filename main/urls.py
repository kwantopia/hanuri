from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^home/$', 'home', name='home_page'),
    url(r'^save/ko/$', 'save_korean', name='save_korean'),
    url(r'^save/en/$', 'save_english', name='save_english'),
)
