# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from urusoro.views import PersonneViewSet, PresenceViewSet, SalaireViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'personnes', PersonneViewSet)
router.register(r'presences', PresenceViewSet)
router.register(r'salaire', SalaireViewSet)


urlpatterns = [
    path("",include(router.urls)),
    path("api_login", include("rest_framework.urls")),
    path("login", TokenObtainPairView.as_view()),
]