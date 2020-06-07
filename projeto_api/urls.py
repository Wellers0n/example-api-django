from django.urls import path
from projeto_api import views

urlpatterns = [
    path('hello/', views.HelloAPIView.as_view()),
]
