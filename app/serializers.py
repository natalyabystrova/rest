from rest_framework import serializers
from .models import Author, Book, Project, ToDo


class AuthorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class AuthorSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'
