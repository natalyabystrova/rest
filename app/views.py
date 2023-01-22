from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Author, Book
from .serializers import AuthorModelSerializer, AuthorSerializer, BookSerializer
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .filters import ProjectFilter, ToDoFilter
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

#class AuthorModelViewSet(ModelViewSet):
    #queryset = Author.objects.all()
    #serializer_class = AuthorModelSerializer


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
    # filterset_fields = ['task', 'created_at']
    pagination_class = ToDoLimitOffsetPagination

    def delete(self, request, pk):
        task = get_object_or_404(ToDo, pk=pk)
        task.deleted = True
        task.save()





