from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	#path(r'example_get/<str:var_a>/<int:var_b>',  views.example_get),
	#path(r'example_post/', views.example_post),
	path(r'fib/', views.fib),
	path(r'multification/', views.multification),
	path(r'picker/', views.picker),
	path(r'DominantColors/', views.domcol),
	path(r'DominantColors/<int:var_c>/', views.domcoll),

]