from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

router=DefaultRouter()

router.register('district',views.DistrictViewSet)
router.register('hotels',views.HotelViewSet)
router.register('reviews',views.ReviewViewSet)
router.register('bookeds',views.BookedViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
if settings.DEBUG:  # Serve media files only in development
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)