
from django.urls import path
from users import views
app_name='users'
urlpatterns = [
    path('',views.Home.as_view(),name='userhome'),
    path('signup',views.Register.as_view(),name='register'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
]
