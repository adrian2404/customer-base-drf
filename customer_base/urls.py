from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views as token_view

from core.views import CustomerViewSet, ProfessionViewSet, DataSheetViewSet, DocumentViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customer")
router.register(r'professions', ProfessionViewSet)
router.register(r'data-sheet', DataSheetViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', token_view.obtain_auth_token)
]
