import graphene
from graphene_django import DjangoObjectType
from ..app.models import Book, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    books_by_author_name = graphene.List(BookType,
                                         name=graphene.String(required=False))

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(id=pk_id)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()
        if name:
            books = books.filter(author__name=name)
        return books


class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, pk_id):
        author = Author.objects.get(pk=pk_id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation()


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
