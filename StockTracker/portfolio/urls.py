from django.urls import path
from .import views  #. indicates import from current directory
urlpatterns = [
    path('', views.home,name='portfolio-home'),
    path('analysis/', views.analysis,name='analysis'),
    
]
