from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Author, Project, ToDo, Book
from .serializers import ProjectModelSerializer, ToDoModelSerializer, AuthorSerializer, BookSerializer, \
    BookSerializerBase, AuthorSerializerBase
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .filters import ProjectFilter, ToDoFilter
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return AuthorSerializerBase
        return AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookSerializer
        return BookSerializerBase


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectListAPIView(ListAPIView, ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPagination

    def delete(self, request, pk):
        task = get_object_or_404(ToDo, pk=pk)
        task.deleted = True
        task.save()
