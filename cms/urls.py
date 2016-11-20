from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^$', views.index, name="cms_index"), # /cms
    url(r'^login$', views.UserLoginView.as_view(), name="cms_login"), # /cms/login
    url(r'^logout$', views.logout_view, name="cms_logout"), # /cms/logout
    url(r'^desejos$', views.list_desejos, name="cms_list_desejos"), # /cms/desejos
    url(r'^desejos/(?P<desejo_id>[0-9]+)$', views.show_desejo, name="cms_show_desejo"), # /cms/desejos/<desejo_id>
]
