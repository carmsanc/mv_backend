from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from serviciosBackend import views

urlpatterns = [
    path('get_token_facebook/', views.Create_User_Facebook.as_view()),

    path('camposantos/', views.CamposantoView.as_view()),
    path('camposanto/<str:pk>/', views.CamposantoViewSet.as_view()),
    path('red_social_post/', views.Red_socialPost.as_view()),
    path('redes_sociales_camp/<str:id_camp>/', views.Red_socialListGet.as_view()),
    path('red_social_put/<str:id_red>/', views.Red_socialPut.as_view()),
    path('geolocalizacion_post/', views.GeolocalizacionPost.as_view()),
    path('geolocalizacion_camp/<str:id_camp>/', views.GeolocalizacionListGet.as_view()),
    path('geolocalizacion_del/<str:id_punto>/', views.GeolocalizacionDelete.as_view()),
    path('sector_camp/<str:id_camp>/', views.SectorListGet.as_view()),
    path('tipo_sepultura_camp/<str:id_camp>/', views.Tipo_sepulturaListGet.as_view()),
    path('difunto_post/', views.DifuntoView.as_view()),
    path('difunto/<str:pk>/', views.DifuntoViewSet.as_view()),
    path('difuntos/<str:id_camp>/', views.DifuntoListGet.as_view()),
    path('difuntos/<str:id_camp>/<str:nombre>/<str:apellido>/', views.DifuntoListFilteredGet.as_view()),
    path('responsable_difunto_post/', views.Responsable_difuntoView.as_view()),
    path('responsable_difunto_get/<str:id_difunto>/', views.Responsable_difuntoViewSet.as_view()),
    path('empresas/', views.EmpresasView.as_view()),
    path('empresa_get/<str:pk>/', views.EmpresaViewSet.as_view()),
    path('usuario/<str:username>/', views.UsuarioViewGet.as_view()),
    path('obtener_usuarios/', views.UsuarioGetAll.as_view()),
    path('usuarios_camp/<str:id_camp>/', views.UsuarioGetCamposanto.as_view()),
    path('listar_permisos_general/', views. PermisoView.as_view()),
    path('mis_user_permisos/<str:id>/', views.User_PermisosGet.as_view()),
    path('user_permisos_post/', views.User_PermisosPost.as_view()),
    #AGREGAR A PA
    path('homenajes/<str:id>/', views.Homenaje_Get.as_view()),
    path('homenajes_post/', views.Homenaje_Set.as_view()),
    path('hmensaje/<str:id>/', views.Htexto_Get.as_view()),
    path('himagen/<str:id>/', views.Himagen_Get.as_view()),
    path('hmensaje_post/', views.Htexto_Set.as_view()),
    path('himagen_post/', views.Himagen_Set.as_view()),
    path('hvideo_post/', views.Hvideo_Set.as_view()),
    path('haudio_post/', views.Haudio_Set.as_view()),
    path('difunto/update-partial/<str:pk>/<str:num_rosas>/',views.AmountPartialUpdateView.as_view()),
    path('historial_rosas/<str:id>/', views.Historial_rosasGet.as_view()),
    path('historial_rosas_post/', views.Historial_rosasSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
