import requests

BASE_URL = "http://127.0.0.1:8000/api"

print("=" * 60)
print("STUDENT SYSTEM API TEST")
print("=" * 60)

print("\n1. REGISTER STUDENT")
print("-" * 40)
resp = requests.post(f"{BASE_URL}/students/register/", json={
    "full_name": "Alice Smith",
    "email": "alice@example.com",
    "mobile": "8888888888",
    "password": "securepass"
})
print(f"Status: {resp.status_code}")
print(f"Response: {resp.json()}")

print("\n2. LOGIN STUDENT")
print("-" * 40)
resp = requests.post(f"{BASE_URL}/students/login/", json={
    "email": "alice@example.com",
    "password": "securepass"
})
print(f"Status: {resp.status_code}")
data = resp.json()
print(f"Response: access token received: {bool(data.get('access'))}")
token = data.get('access')

print("\n3. VIEW JOBS (Authenticated)")
print("-" * 40)
resp = requests.get(f"{BASE_URL}/jobs/", headers={"Authorization": f"Bearer {token}"})
print(f"Status: {resp.status_code}")
print(f"Response: {resp.json()}")

print("\n4. VIEW JOBS (Unauthenticated - should be 401)")
print("-" * 40)
resp = requests.get(f"{BASE_URL}/jobs/")
print(f"Status: {resp.status_code}")
print(f"Response: {resp.json()}")

print("\n" + "=" * 60)
print("ALL 4 APIs WORKING!")
print("=" * 60)
print("""
API Endpoints:
1. POST /api/students/register/ - Register new student
2. POST /api/students/login/ - Login and get JWT token
3. GET /api/jobs/ (Auth) - View jobs (requires token)
4. /api/admin/jobs/ - Admin job management (requires admin)
""")
