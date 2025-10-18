import os
import requests

# URL nguồn dữ liệu
url = "https://raw.githubusercontent.com/nguyen-toan/ISLR/master/dataset/Advertising.csv"

# Đường dẫn lưu file
target_dir = os.path.join("engaged_polliwog", "feature_repo", "data")
target_path = os.path.join(target_dir, "Advertising.csv")

def download_csv():
    # Tạo thư mục nếu chưa có
    os.makedirs(target_dir, exist_ok=True)

    print(f"📥 Đang tải dữ liệu từ: {url}")
    response = requests.get(url)
    response.raise_for_status()  # báo lỗi nếu tải không thành công

    # Ghi file
    with open(target_path, "wb") as f:
        f.write(response.content)

    print(f"✅ Đã lưu file vào: {target_path}")

if __name__ == "__main__":
    download_csv()
