# feature_repo/feature_view.py
from feast import Entity, FeatureView, Field, FileSource, ValueType
from datetime import timedelta
from feast.types import Float32

# Nguồn dữ liệu (parquet) đã tạo ở bước trên
advertising_source = FileSource(
    path="data/Advertising.parquet",
    event_timestamp_column="event_timestamp",
)

# Entity: ad_id
ad_entity = Entity(
    name="ad_id",
    value_type=ValueType.INT64,
    description="ID of the advertising sample"
)

# FeatureView: chứa các feature TV, Radio, Newspaper
ad_feature_view = FeatureView(
    name="ad_features",
    entities=[ad_entity],
    ttl=timedelta(days=3650),  # không quan trọng ở ví dụ này
    schema=[
        Field(name="TV", dtype=Float32),
        Field(name="Radio", dtype=Float32),
        Field(name="Newspaper", dtype=Float32),
        Field(name="Sales", dtype=Float32),  # ta có Sales luôn trong historical
    ],
    source=advertising_source,
    online=True,
    description="Feature view for advertising data",
    tags= {"owner": "TEAM CONQ26", "version": "1.0"}
)
