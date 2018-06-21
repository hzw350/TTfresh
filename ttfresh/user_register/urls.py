from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^info/$', views.info),
    url(r'^user_order/$', views.user_order),
    url(r'^user_site/$', views.user_site),
    url(r'^logout/$', views.logout),
    url(r'^user_site_handle/$',views.user_site_handle)
]