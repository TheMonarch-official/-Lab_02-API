# Sentiment Analysis API (FastAPI + Hugging Face)

Practice 01 – Application Programming Interface

Computational Thinking

Đại học Khoa học Tự nhiên – ĐHQG-HCM.

**Họ tên:** `Võ Thiên Khánh` – MSSV `25127377`

## Model

[`distilbert/distilbert-base-uncased-finetuned-sst-2-english`](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) – phân loại cảm xúc câu **tiếng Anh** thành `POSITIVE` hoặc `NEGATIVE`.

## Chức năng

| Endpoint | Mô tả |
|---|---|
| `GET /` | Giới thiệu API |
| `GET /health` | Kiểm tra trạng thái |
| `POST /predict` | Nhận `{"text": "..."}`, trả về `label` và `score` (JSON) |

Lỗi được xử lý: text rỗng hoặc quá dài (`400`), thiếu trường `text` (`422`), model lỗi (`500`).

## Cài đặt và chạy

```bash
python -m venv venv
venv\Scripts\activate            # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Server chạy tại `http://127.0.0.1:8000` (tài liệu tương tác: `/docs`). Lần chạy đầu sẽ tự tải model (~270 MB), cần internet.

## Gọi API

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this movie!"}'
```

```json
{"input": "I love this movie!", "label": "POSITIVE", "score": 0.9999}
```

Text rỗng (`{"text": ""}`) trả về `400`:

```json
{"detail": "Text must not be empty."}
```

Chạy bộ test bằng `requests` (khi server đang chạy): `python test_api.py`

## Video demo

