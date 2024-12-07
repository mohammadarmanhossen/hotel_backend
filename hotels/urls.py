from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router=DefaultRouter()

router.register('district',views.DistrictViewSet)
router.register('hotels',views.HotelViewSet)
router.register('reviews',views.ReviewViewSet)
router.register('bookeds',views.BookedViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
