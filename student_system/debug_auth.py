import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_system.settings')
django.setup()

from students.models import Students
from students.authentication import StudentJWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
import traceback

s = Students.objects.first()
print(f"Student: {s}, pk={s.pk}")

refresh = RefreshToken.for_user(s)
access_str = str(refresh.access_token)
print(f"Access token: {access_str[:60]}...")

auth = StudentJWTAuthentication()
print("\n1. Calling get_validated_token...")
try:
    validated = auth.get_validated_token(access_str)
    print(f"   Success")
except Exception as e:
    print(f"   Error: {e}")
    traceback.print_exc()
    exit(1)

print("\n2. Calling get_user...")
try:
    user = auth.get_user(validated)
    print(f"   Success: {user}")
except Exception as e:
    print(f"   Error: {e}")
    traceback.print_exc()
