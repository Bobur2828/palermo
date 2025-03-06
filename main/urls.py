from django.urls import path
from main.views.homePG import HomePGView
from main.views.aboutPG import AboutPGView
urlpatterns = [
    path('home/<str:lang>/',HomePGView.as_view()),
    path('about/<str:lang>/', AboutPGView.as_view()),

]