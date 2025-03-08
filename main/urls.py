from django.urls import path
from main import views
urlpatterns = [
    path('home/<str:lang>/',views.HomeHeaderAPIView.as_view()),

]