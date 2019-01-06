from django.conf.urls import url
from intf import views

urlpatterns = [
	url(r'^$',views.index),
]