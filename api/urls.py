from django.conf.urls import url
from api.views import UserListCreateApiView, UserRetriveUpdateDestroyApiView

urlpatterns = [
    #url(r'^$', views.index, name="cms_index"), # /api
    url(r'^usuarios/$', UserListCreateApiView.as_view(), name="api_list_create_update_destroy_usuarios"), # /api/usuarios
    url(r'^usuarios/(?P<pk>[0-9]+)$', UserRetriveUpdateDestroyApiView.as_view(), name="api_retrieve_update_destroy_usuario"), # /api/usuarios/<pk>
    #url(r'^login$', views.UserLoginView.as_view(), name="cms_login"), # /cms/login
    #url(r'^logout$', views.logout_view, name="cms_logout"), # /cms/logout
    #url(r'^desejos$', views.list_desejos, name="cms_list_desejos"), # /cms/desejos
    #url(r'^desejos/(?P<desejo_id>[0-9]+)$', views.show_desejo, name="cms_show_desejo"), # /cms/desejos/<desejo_id>
]
