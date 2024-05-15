from rest_framework import viewsets, mixins,filters
from rest_framework import response 
from .serializers import *
from rest_framework.permissions import *
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication 
from django_filters.rest_framework import DjangoFilterBackend

class IsAuthenticatedForReadOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if request.method in ["GET", "PUT", "PATCH"]:
                return True
        if user.is_superuser:
            return True
        return False

class PresenceViewSet(viewsets.ModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    permission_classes = IsAuthenticatedForReadOrIsAdmin,
    authentication_classes = JWTAuthentication, SessionAuthentication

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class PersonneViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    ):
    queryset = Personne.objects.filter(is_deleted = False)
    serializer_class = PersonneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "nom": ["iexact"],
        "id": ["exact"],
    }
    search_fields = ["prenom"]

    def delete(self, request, pk):
        instance:Personne = self.get_object()
        instance.is_deleted = True
        instance.save()
        return response(None, 204)
    
class SalaireViewSet(viewsets.ModelViewSet):
    queryset = Salaire.objects.all()
    serializer_class = SalaireSerializer
    permission_classes = IsAuthenticatedForReadOrIsAdmin,
    authentication_classes = JWTAuthentication, SessionAuthentication

    def perform_create(self, serializer):
        data = serializer.validate_data
        personne = data["personne"]
        Presence = Presence.objects.filter(personne=personne).count()
        montant = Presence * personne.salaire
        serializer.save(created_by = self.request.user, montant = 0)

