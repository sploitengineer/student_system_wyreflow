import requests

BASE_URL = "http://127.0.0.1:8000/api"

print("TEST 1: Register")
resp = requests.post(f"{BASE_URL}/students/register/", json={
    "full_name": "Test User 3",
    "email": "test3@test.com",
    "mobile": "7777777777",
    "password": "pass123"
})
print(f"  Status: {resp.status_code}")

print("\nTEST 2: Login")
resp = requests.post(f"{BASE_URL}/students/login/", json={
    "email": "john@gmail.com",
    "password": "123456"
})
print(f"  Status: {resp.status_code}")
token = resp.json().get('access')
print(f"  Token: {'received' if token else 'missing'}")

print("\nTEST 3: View Jobs (with auth)")
resp = requests.get(f"{BASE_URL}/jobs/", headers={"Authorization": f"Bearer {token}"})
print(f"  Status: {resp.status_code}")
print(f"  Response: {resp.text[:200]}")

print("\nTEST 4: View Jobs (no auth)")
resp = requests.get(f"{BASE_URL}/jobs/")
print(f"  Status: {resp.status_code}")
