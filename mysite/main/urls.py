from . import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('run_neural_network/', views.run_neural_network, name='run_neural_network'),
]
