from django.conf.urls import url
from api.views_usuarios import UserListCreateApiView, UserRetrieveUpdateDestroyApiView
from api.views_desejos import DesejoListCreateApiView, DesejoRetrieveUpdateDestroyApiView

urlpatterns = [
    #url(r'^$', views.index, name="cms_index"), # /api
    url(r'^usuarios/$', UserListCreateApiView.as_view(), name="api_list_create_usuarios"), # /api/usuarios
    url(r'^usuarios/(?P<pk>[0-9]+)$', UserRetrieveUpdateDestroyApiView.as_view(), name="api_retrieve_update_destroy_usuario"), # /api/usuarios/<pk>
    url(r'^desejos/$', DesejoListCreateApiView.as_view(), name="api_list_create_desejos"), # /api/desejos
    url(r'^desejos/(?P<pk>[0-9]+)$', DesejoRetrieveUpdateDestroyApiView.as_view(), name="api_retrieve_update_destroy_desejo"), # /api/desejos/<pk>
]
