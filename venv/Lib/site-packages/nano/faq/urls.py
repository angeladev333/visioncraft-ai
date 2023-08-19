from django.conf.urls import url

from nano.faq import views


urlpatterns = [
    url(r'^$',     views.list_faqs),
]
