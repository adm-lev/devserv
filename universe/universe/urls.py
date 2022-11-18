from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import universe.views
from todos.views import UserCustomViewSet, ProjectCustomViewSet, TodoCustomViewSet, UserModelViewSet
from rest_framework.authtoken import views as token_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from graphene_django.views import GraphQLView
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectCustomViewSet)
router.register('todos', TodoCustomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', universe.views.homePageView),
    # path('test/', universe.views.testPageView),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', token_view.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'), 
    path('graphql/', GraphQLView.as_view(graphiql=True)),   
    path('', TemplateView.as_view(template_name='index.html')),
    path('users/', TemplateView.as_view(template_name='index.html')),
]
