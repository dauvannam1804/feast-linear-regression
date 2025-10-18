from feast import FeatureStore
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# load feature store (tự động dùng feature_repo/feature_store.yaml)
store = FeatureStore(repo_path="engaged_polliwog/feature_repo")

# đọc file parquet để tạo entity dataframe (ad_id + event_timestamp)
entity_df = pd.read_parquet("engaged_polliwog/feature_repo/data/Advertising.parquet")[["ad_id", "event_timestamp"]]

# get_historical_features: list features dưới dạng "feature_view:feature_name"
feature_refs = [
    "ad_features:TV",
    "ad_features:Radio",
    "ad_features:Newspaper",
    "ad_features:Sales",
]

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=feature_refs
).to_df()

# kết quả thường có ad_id, event_timestamp, và các cột feature
print("Lấy dữ liệu training từ Offline Store...")
print("Historical data shape:", training_df.shape)
print(training_df.head())

# chuẩn bị X, y
X = training_df[["TV", "Radio", "Newspaper"]]
y = training_df["Sales"]

# chia train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train linear regression
print("\nBắt đầu huấn luyện mô hình...")
model = LinearRegression()
model.fit(X_train, y_train)

# preds
y_pred = model.predict(X_test)

print("\n--- Kết quả đánh giá mô hình ---")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# lưu model
joblib.dump(model, "linear_model.pkl")
print("Saved linear_model.pkl")
