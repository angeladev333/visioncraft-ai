from django.conf.urls import url

from nano.badge import views

urlpatterns = [
    url(r'^$',                 views.list_badges, name='badge-list'),
    url(r'^(?P<pk>[0-9]+)/$',  views.show_badge, name='badge-detail'),
]
