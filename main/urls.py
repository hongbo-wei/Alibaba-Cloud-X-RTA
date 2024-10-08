from django.urls import path
from . import views
from .utils import update_like, update_love


urlpatterns = [
    path('', views.index, name='index'),
    path('heatmap/', views.heatmap, name='heatmap'),
    path('update_like/', update_like, name='update_like'),
    path('update_love/', update_love, name='update_love'),
    # path('accessibility/', views.accessibility, name='accessibility'),
]   
