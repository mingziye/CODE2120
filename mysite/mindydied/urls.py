from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	 path('admin/', admin.site.urls),
    path(r'example/', include('example.urls')),
    path(r'Mindy_Ye/', include('mindydied.urls')),

]