from django.urls import path
from rest_framework.routers import DefaultRouter
from profiles_api import views
from django.urls import include

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [ 
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
    