from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
<<<<<<< HEAD
]
=======
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
]
>>>>>>> e5c513e83a95d223e9e20dd26b9f80dc8e000af3
