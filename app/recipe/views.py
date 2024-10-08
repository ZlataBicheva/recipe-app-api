"""
Views for the recipe APIs
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):

    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class forr request."""
        if self.action == 'list':
            return serializers.RecipeDetailSerializer

        return self.serializer_class

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class