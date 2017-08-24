from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^logout$', views.logout),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^unsubscribe$', views.unsubscribe),
	url(r'^member$', views.member),
	url(r'^cart$', views.cart),

]
