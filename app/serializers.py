from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author
from rest_framework import serializers
from .models import Author, Book, Project, ToDo

class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name' 'birthday_year')


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'