from django.conf.urls import url

from nano.mark import views


urlpatterns = [
    url(r'^toggle$',    views.toggle_mark, name='toggle_mark'),
]
