from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import universe.views
from todos.views import UserCustomViewSet, ProjectCustomViewSet, TodoCustomViewSet

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectCustomViewSet)
router.register('todos', TodoCustomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', universe.views.homePageView),
    path('test/', universe.views.testPageView),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
