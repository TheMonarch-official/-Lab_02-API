import requests

BASE_URL = "http://127.0.0.1:8000"


def show(title, response):
    print(f"--- {title} ---")
    print("Status code:", response.status_code)
    print("Response   :", response.json())
    print()


# 1. GET /
show("GET /", requests.get(f"{BASE_URL}/"))

# 2. GET /health
show("GET /health", requests.get(f"{BASE_URL}/health"))

# 3. POST /predict với nhiều input khác nhau
for text in ["I love this movie!", "This is the worst day ever."]:
    r = requests.post(f"{BASE_URL}/predict", json={"text": text})
    show(f"POST /predict: {text}", r)

# 4. Các trường hợp lỗi
show("Lỗi: text rỗng", requests.post(f"{BASE_URL}/predict", json={"text": ""}))
show("Lỗi: thiếu trường text", requests.post(f"{BASE_URL}/predict", json={}))
show("Lỗi: gọi GET vào /predict", requests.get(f"{BASE_URL}/predict"))