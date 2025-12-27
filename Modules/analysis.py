import pandas as pd

def analyze_accidents(df: pd.DataFrame):
    """
    Phân tích dữ liệu tai nạn giao thông:
    - Theo thành phố
    - Theo khung giờ
    - Theo mức độ nghiêm trọng (Severity)
    """

    results = {}

    # ===============================
    # 1. Tổng số tai nạn theo thành phố
    # ===============================
    accidents_by_city = (
        df.groupby("City")
          .size()
          .sort_values(ascending=False)
    )

    results["accidents_by_city"] = accidents_by_city

    # ===============================
    # 2. Phân tích theo khung giờ
    # ===============================
    # Nếu chưa có cột Hour thì tạo
    if "Hour" not in df.columns:
        df["Hour"] = pd.to_datetime(df["Start_Time"]).dt.hour

    accidents_by_hour = (
        df.groupby("Hour")
          .size()
          .sort_index()
    )

    results["accidents_by_hour"] = accidents_by_hour

    # ===============================
    # 3. Phân tích theo mức độ nghiêm trọng
    # ===============================
    severity_count = df["Severity"].value_counts().sort_index()

    severity_percentage = round(
        severity_count / severity_count.sum() * 100,
        2
    )

    results["severity_count"] = severity_count
    results["severity_percentage"] = severity_percentage

    return results
