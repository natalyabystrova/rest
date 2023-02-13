from app import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.apps import MainappConfig
from app.views import AuthorViewSet, BookViewSet

app_name = MainappConfig.name

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('projectlist/', views.ProjectListAPIView.as_view(), name="contacts"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]