from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views
from review_data.views import index,generic
#from review_data.views import elements

#index == movie_list
#generic == movie_detail

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^movie/(?P<no>\d+)/$', views.generic, name = 'generic'),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
