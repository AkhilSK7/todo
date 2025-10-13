"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path('addtask',views.addtask,name="addtask"),
    path('viewtask',views.viewtask,name="viewtask"),
    path('done/<int:task_id>/',views.donetask,name='done_task'),
    path('delete/<int:task_id>/',views.deletetask,name='delete_task'),
    path('filter',views.filtertask,name='filter_task'),
]
