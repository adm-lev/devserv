from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import universe.views
from todos.views import UserCustomViewSet, ProjectCustomViewSet, TodoCustomViewSet
from rest_framework.authtoken import views as token_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectCustomViewSet)
router.register('todos', TodoCustomViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', universe.views.homePageView),
    path('test/', universe.views.testPageView),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', token_view.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'),    
]
