from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('signup', views.SignUpView)

urlpatterns = router.urls