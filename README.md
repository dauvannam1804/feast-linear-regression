# 🚀 Feast Linear Regression

Dự án này minh họa cách **xây dựng và triển khai Feature Store cục bộ bằng Feast** để huấn luyện và dự đoán mô hình hồi quy tuyến tính (Linear Regression) dựa trên bộ dữ liệu **Advertising**.

---

## 🧩 1. Cài đặt môi trường

### Tạo môi trường ảo và cài đặt thư viện cần thiết:
```bash
uv add -r requirements.txt
source .venv/bin/activate
```

---

## 🏗️ 2. Khởi tạo dự án Feast

Khởi tạo cấu trúc dự án Feast:
```bash
feast init
```

---

## 📥 3. Tải dữ liệu Advertising

Tải file **Advertising.csv** từ GitHub và lưu vào thư mục `feature_repo/data`:
```bash
python download_data.py
```

---

## 🧮 4. Chuẩn bị dữ liệu

Thêm một số trường bổ sung và chuyển đổi dữ liệu sang định dạng **Parquet**:
```bash
python prepare_data.py
```

---

## ⚙️ 5. Áp dụng định nghĩa Feature Store

Di chuyển vào thư mục Feature Store:
```bash
cd engaged_polliwog/feature_repo
```

Áp dụng các định nghĩa trong repo:
```bash
feast apply
```

---

## 🧱 6. Nạp dữ liệu vào Online Store

**Materialize** – nạp dữ liệu lịch sử vào Online Store:
```bash
feast materialize $(date -d '1 year ago' +%Y-%m-%d) $(date +%Y-%m-%d)
```

---

## 🧠 7. Huấn luyện mô hình

Lấy dữ liệu offline và huấn luyện mô hình hồi quy tuyến tính:
```bash
python train_model.py
```

---

## ⚡ 8. Dự đoán với dữ liệu Online

Truy xuất feature online và thực hiện dự đoán:
```bash
python predict_online.py
```

---

## 🌐 9. Khám phá Feast UI

Khởi chạy giao diện web để trực quan hóa Feature Store:
```bash
cd feature_repo
feast ui
```

---

## 📘 Tổng quan quy trình

1. **Feast** lưu trữ dữ liệu huấn luyện trong **Offline Store (Parquet)** và phục vụ real-time qua **Online Store (SQLite)**.  
2. **Huấn luyện mô hình** từ dữ liệu offline.  
3. **Truy xuất features online** để dự đoán theo thời gian thực.  
4. **Khám phá Feast UI** để xem cấu trúc và dữ liệu Feature Store.

---