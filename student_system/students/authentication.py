from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from .models import Students

class StudentJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get(api_settings.USER_ID_CLAIM)
        if user_id is None:
            return None
        try:
            return Students.objects.get(pk=user_id)
        except Students.DoesNotExist:
            return super().get_user(validated_token)
