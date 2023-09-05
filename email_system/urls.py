# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EventViewSet, EmailTemplateViewSet, EmailLogViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'events', EventViewSet)
router.register(r'email-templates', EmailTemplateViewSet)
router.register(r'email-logs', EmailLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
