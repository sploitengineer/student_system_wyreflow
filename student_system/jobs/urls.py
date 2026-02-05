from rest_framework.routers import DefaultRouter
from .views import JobAdminViewSet, JobListView
from django.urls import path, include

router = DefaultRouter()
router.register('admin/jobs', JobAdminViewSet, basename='admin-jobs')

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/', JobListView.as_view(), name='job-list'),
]
