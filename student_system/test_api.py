import requests

BASE_URL = "http://127.0.0.1:8000/api"

print("=" * 50)
print("TEST 2: Login Student (john@gmail.com)")
print("=" * 50)

resp = requests.post(f"{BASE_URL}/students/login/", json={
    "email": "john@gmail.com",
    "password": "123456"
})
print(f"Status: {resp.status_code}")
data = resp.json()
print(f"Response: {data}")
access_token = data.get('access')
print(f"Token: {access_token[:50]}..." if access_token else "No token")

if access_token:
    print("\n" + "=" * 50)
    print("TEST 3: View Jobs (Authenticated)")
    print("=" * 50)
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(f"{BASE_URL}/jobs/", headers=headers)
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")
