from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from store.models import Books, UserBookRelation
from store.permisions import IsOwnerOrOwnerOrReadOnly
from store.serialiser import BooksSerializer, UserRelationSerializer


class ViewSerializer(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsOwnerOrOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        serializer.validate_data['owner'] = self.request.user
        serializer.save()


class BookRelationView(UpdateModelMixin, GenericViewSet):
    queryset = UserBookRelation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRelationSerializer
    lookup_field = 'book'

def oauth(request):
    return render(request, 'oauth.html')
