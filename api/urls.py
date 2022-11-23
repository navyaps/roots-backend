from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (BlacklistTokenView,LoggedInUserView,RegisterView,TrendingViewSet,PlaceView,ActivitiesView)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router=DefaultRouter()
router.register('register',RegisterView,basename='register')
router.register('trendings',TrendingViewSet,basename='trendings')
router.register('places',PlaceView,basename='places')
router.register('activities',ActivitiesView,basename='activities')


urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
]