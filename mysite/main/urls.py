from . import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('classify_comment', views.classify_comment, name='classify_comment'),
]
