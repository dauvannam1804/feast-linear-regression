from feast import FeatureStore
import pandas as pd
import joblib

# 1. Load model & feature store
model = joblib.load("linear_model.pkl")
store = FeatureStore(repo_path="engaged_polliwog/feature_repo")

# 2. Giả lập dự đoán cho một ad_id mới (ví dụ: ad_id = 0)
ad_id = 0

# 3. Lấy feature trực tiếp từ Online Store
feature_refs = [
    "ad_features:TV",
    "ad_features:Radio",
    "ad_features:Newspaper",
]

# entity_rows là danh sách các entity cần lấy feature
entity_rows = [{"ad_id": ad_id}]

# get_online_features — lấy feature mới nhất từ Redis (hoặc online backend khác)
online_features = store.get_online_features(
    features=feature_refs,
    entity_rows=entity_rows
).to_dict()

# 4. Chuyển sang DataFrame để feed vào model
features_df = pd.DataFrame.from_dict(online_features)
x = pd.DataFrame(
    [features_df[["TV", "Radio", "Newspaper"]].iloc[0].values],
    columns=["TV", "Radio", "Newspaper"]
)
# 5. Dự đoán
pred = model.predict(x)
print(f"Predicted Sales for ad_id={ad_id}: {pred[0]:.2f}")

