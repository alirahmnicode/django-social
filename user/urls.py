from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('signup', views.SignUpView)

urlpatterns = [
    path('activate/', views.ActivateAcoountView.as_view()),
    path('profile/<int:pk>/', views.ProfileView.as_view()),
    path('search/', views.SearchApiView.as_view()),
]

urlpatterns += router.urls
