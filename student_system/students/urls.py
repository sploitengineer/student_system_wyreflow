from django.urls import path
from .views import RegisterStudentView, LoginStudentView

urlpatterns = [
    path('register/', RegisterStudentView.as_view(), name='register-student'),
    path('login/', LoginStudentView.as_view(), name='login-student'),
]