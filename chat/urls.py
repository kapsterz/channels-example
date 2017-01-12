from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^selchat/$', views.selchat, name='selchat'),
    url(r'^success/$', views.success, name='success'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
