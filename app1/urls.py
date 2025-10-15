
from django.urls import path
from app1 import views
app_name='app1'
urlpatterns = [
    path("",views.home,name="home"),
    path('addtask',views.addtask,name="addtask"),
    path('viewtask',views.viewtask,name="viewtask"),
    path('done/<int:task_id>/',views.donetask,name='done_task'),
    path('delete/<int:task_id>/',views.deletetask,name='delete_task'),
    path('filter',views.filtertask,name='filter_task'),
]