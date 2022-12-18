from django.contrib import admin
from django.urls import path
from djangoKeys2APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"),
    path("create",views.create,name = "create")
]
