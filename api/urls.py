from django.conf.urls import url 
from api import views 
 
urlpatterns = [ 
    url(r'^api/post$', views.post_blog),
    url(r'^api/$', views.edit_blog)
]
