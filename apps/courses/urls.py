from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/add_course$', views.add_course),
    url(r'^courses/destroy/(?P<id>\d+)$', views.to_remove),
    url(r'^courses/remove/(?P<id>\d+)$', views.destroy),

    # url(r'^users/(?P<returned_id>\d+)$', views.show),
]
