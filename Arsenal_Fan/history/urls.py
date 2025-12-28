from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.history_home, name='history_home'),  # /history/
    path('milestones/', views.milestones, name='milestones'),  # /history/milestones/
    path('legends/', views.legends, name='legends'),  # /history/legends/
    path('trophies/', views.trophies, name='trophies'),  # /history/trophies/
    path('legend/<int:pk>/', views.legend_detail, name='legend_detail'),  # /history/legend/1/
]