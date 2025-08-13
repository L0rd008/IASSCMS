from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_view),
    path('predict/', views.predict_view),
]
