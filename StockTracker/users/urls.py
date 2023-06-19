from django.urls import path
from .import views  #. indicates import from current directory
urlpatterns = [
    path('register/', views.register,name='user-register'),
    path('logout/', views.logout_view,name='user-logout'),
    path('login/', views.login_view,name='user-login'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),  

]
